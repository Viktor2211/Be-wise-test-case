from pydantic import BaseModel, Field

class QuestionRequest(BaseModel):
    questions_num: int = Field(gt=0)