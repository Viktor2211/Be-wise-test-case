from database import Base
from sqlalchemy import Column, Integer, String, DateTime



class Question(Base):
    __tablename__='questions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text_question = Column(String)
    text_answer = Column(String)
    creation_date = Column(String)


