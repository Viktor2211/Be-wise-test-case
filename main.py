from fastapi import FastAPI, status, Depends
import requests
from schemas import QuestionRequest
import models
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/quiz/get_questions/", status_code=status.HTTP_200_OK)
async def get_questions(db: db_dependency):
    return db.query(models.Question).all()


@app.post("/quiz/create_questions/", status_code=status.HTTP_201_CREATED)
async def create_questions(db: db_dependency, question_request: QuestionRequest):
    url_for_questions = f"https://jservice.io/api/random?count={question_request.questions_num}"
    response = requests.get(url_for_questions).json()
    for quiz_question in response:
        question_model = models.Question()
        question_model.id = quiz_question.get("id")
        question_model.text_answer = quiz_question.get("answer")
        question_model.text_question = quiz_question.get("question")
        question_model.creation_date = quiz_question.get("created_at")
        db.add(question_model)
        db.commit()
    return response
