import requests
import json
from .config import ACCESS_TOKEN
from .models import WeatherInfo
from .exceptions import ConnectionResponseError
from .exceptions import HttpCodeResponseError
from .exceptions import InvalidJsonResponseError
from .exceptions import ServiceResponseError
from .exceptions import DataNotContainedResponseError
from .exceptions import MalformedDataResponseError

# Weather Stack API template
API_URI = 'http://api.weatherstack.com/current?access_key={}&query={:05d}'


def get_current_weather(zip_code: int) -> WeatherInfo:
    """
    This function will get weather information from Weather Stack API.

    :param zip_code: zip_code for query
    :return: Weather information in object. If any error occurs, return None and error will be logged by logging system
    """
    try:
        response = requests.get(API_URI.format(ACCESS_TOKEN, zip_code))
    except requests.exceptions.RequestException as e:
        raise ConnectionResponseError(
            f'Connection error. {e}'
        )

    # Check if status code of response is not HTTP_200 to handle error
    if response.status_code != 200:
        raise HttpCodeResponseError(
            f'Status code {response.status_code}'
        )

    # Check if parse json successful to handle error
    try:
        response_data = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        raise InvalidJsonResponseError(
            f'Response is not in JSON format. Response: {response.text}'
        )

    # Check if 'error' is in response data to handle error
    if 'error' in response_data:
        raise ServiceResponseError(
            f'Response contains error. Response: {json.dumps(response_data["error"])}'
        )

    # Check if 'current' is not in response data to handle error
    if 'current' not in response_data or not response_data['current']:
        raise DataNotContainedResponseError(
            f'"current" field to get weather info is not in the response. Response: {json.dumps(response_data)}'
        )

    # Validate and create Weather Info instance to return or handle error if fail to validate
    try:
        return WeatherInfo.from_data(response_data['current'])
    except ValueError as e:
        raise MalformedDataResponseError(
            f'Malformed weather data structure. {e}'
        )

