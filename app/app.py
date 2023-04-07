import logging

from .config import QUESTIONS
from .config import EQuestion
from .utils import preprocess_input
from .api import get_current_weather
from .services import should_go_outside
from .services import should_wear_sunscreen
from .services import can_fly_kite
from .exceptions import APIRequestError


# Preprocessing configured questions
HANDLED_QUESTIONS = [preprocess_input(question) for question in QUESTIONS]


def _find_question(question: str) -> EQuestion:
    """
    :param question: The question of user
    :return: Handled case question enum found. If not found any case, return UNKNOWN
    """
    # Preprocessing for user question before matching
    handled_question = preprocess_input(question)
    # Find corresponding index
    for idx, question in enumerate(HANDLED_QUESTIONS):
        if handled_question == question:
            return EQuestion(idx)
    # Not found
    return EQuestion.UNKNOWN


def answer(zip_code: int, question: str) -> str:
    """
    :param zip_code: Zip code for get weather information
    :param question: The input question from user
    :return: The answer of program for corresponding question
    """
    # Find the handled question index for the input
    question_type = _find_question(question)
    # If not found the handled case, response no idea
    if question_type == EQuestion.UNKNOWN:
        return "I don't know"
    # Get weather information
    try:
        weather_info = get_current_weather(zip_code)
    except APIRequestError as e:
        logging.error(f'Request API. {e}')
        raise e
    logging.info(f'Weather Info: {weather_info.__dict__}')
    # So if everything ok, find the answer for user:
    # Should I go outside?
    if question_type == EQuestion.SHOULD_I_GO_OUTSIDE:
        return "YES" if should_go_outside(weather_info) else "NO"
    # Should I wear sunscreen?
    elif question_type == EQuestion.SHOULD_I_WEAR_SUNSCREEN:
        return "YES" if should_wear_sunscreen(weather_info) else "NO"
    # Can I fly my kite?
    elif question_type == EQuestion.CAN_I_FLY_MY_KITE:
        return "YES" if can_fly_kite(weather_info) else "NO"
    # This case for defensive
    else:
        return "I don't know"

