from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    external_id = Column(Integer)
    text_question = Column(String)
    text_answer = Column(String)
    created_at = Column(String)
