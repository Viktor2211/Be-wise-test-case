import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from app.exceptions import JServiceException
from app.models import Question


def query(url: str, params: dict) -> list:
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["POST"],
        backoff_factor=1,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    try:
        response = session.get(url=url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except (
        requests.exceptions.RequestException,
        requests.exceptions.JSONDecodeError,
        KeyError,
    ) as e:
        raise JServiceException(e)


def get_or_create(session, question: Question):
    instance = session.query(Question).filter(
        Question.text_question == question.text_question).first()
    if instance:
        return False
    else:
        session.add(question)
        session.commit()
        return True
