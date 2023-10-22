from datetime import datetime
from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    questions_num: int = Field(gt=0)


class JServiceData(BaseModel):
    obj_id: int = Field(alias="id")
    answer: str
    question: str
    created_at: datetime
