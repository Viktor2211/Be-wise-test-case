from fastapi import FastAPI, status, Depends
from app.schemas import QuestionRequest, JServiceData
from app import models
from app.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from app.services import query, get_or_create

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/questions", status_code=status.HTTP_201_CREATED)
async def questions(db: db_dependency, request: QuestionRequest):
    current_number = request.questions_num
    while current_number > 0:
        data = query(
            url="https://jservice.io/api/random",
            params={'count': current_number},
        )

        quiz_list = [JServiceData.model_validate(datum) for datum in data]

        for quiz in quiz_list:
            instance = models.Question()
            instance.external_id = quiz.obj_id
            instance.text_answer = quiz.answer
            instance.text_question = quiz.question
            instance.created_at = quiz.created_at
            unrecorded = get_or_create(question=instance, session=db)
            if unrecorded:
                current_number -= 1
            else:
                continue

    previous_record = db.query(models.Question).order_by(
        models.Question.id.desc()).first()

    if previous_record:
        return previous_record
    return {}
