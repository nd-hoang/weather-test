import unittest
import json
from unittest.mock import MagicMock, patch
from app.config import ACCESS_TOKEN
from app.api import API_URI, get_current_weather
from app.exceptions import HttpCodeResponseError
from app.exceptions import InvalidJsonResponseError
from app.exceptions import ServiceResponseError
from app.exceptions import DataNotContainedResponseError
from app.exceptions import MalformedDataResponseError


class TestAPI(unittest.TestCase):
    @patch('app.api.requests')
    def test_request_api_successfully(self, mock_requests):
        # Setup requests mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "request": {
                "type": "Zipcode",
                "query": "30076",
                "language": "en",
                "unit": "m"
            },
            "location": {
                "name": "Roswell",
                "country": "USA",
                "region": "Georgia",
                "lat": "34.026",
                "lon": "-84.312",
                "timezone_id": "America\/New_York",
                "localtime": "2023-04-06 10:39",
                "localtime_epoch": 1680777540,
                "utc_offset": "-4.0"
            },
            "current": {
                "observation_time": "02:39 PM",
                "temperature": 22,
                "weather_code": 116,
                "weather_icons": [
                    "https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0002_sunny_intervals.png"
                ],
                "weather_descriptions": ["Partly cloudy"],
                "wind_speed": 4,
                "wind_degree": 253,
                "wind_dir": "WSW",
                "pressure": 1024,
                "precip": 0,
                "humidity": 81,
                "cloudcover": 75,
                "feelslike": 22,
                "uv_index": 6,
                "visibility": 16,
                "is_day": "yes"
            }
        })
        mock_requests.get.return_value = mock_response

        # Run function
        actual = get_current_weather(30076)

        # Check if call request get with correct parameters
        mock_requests.get.assert_called_with(API_URI.format(ACCESS_TOKEN, 30076))
        # Check if result is not None
        self.assertIsNotNone(actual)
        # Check if result has correct values
        self.assertEqual(actual.weather_code, 116)
        self.assertEqual(actual.wind_speed, 4)
        self.assertEqual(actual.uv_index, 6)
        self.assertEqual(actual.temperature, 22)
        self.assertEqual(actual.humidity, 81)

    @patch('app.api.requests')
    def test_request_api_error_with_status_code(self, mock_requests):
        # Setup requests mock
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response

        # Run function should raise error because of http code 500
        self.assertRaises(HttpCodeResponseError, lambda: get_current_weather(30076))

        # Check if call request get with correct parameters
        mock_requests.get.assert_called_with(API_URI.format(ACCESS_TOKEN, 30076))

    @patch('app.api.requests')
    def test_request_api_error_with_not_json_format_response(self, mock_requests):
        # Setup requests mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html></html>'
        mock_requests.get.return_value = mock_response

        # Run function should raise error because API returns error field in response
        self.assertRaises(InvalidJsonResponseError, lambda: get_current_weather(30076))

        # Check if call request get with correct parameters
        mock_requests.get.assert_called_with(API_URI.format(ACCESS_TOKEN, 30076))

    @patch('app.api.requests')
    def test_request_api_error_with_error_in_the_response(self, mock_requests):
        # Setup requests mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "success": False,
            "error": {
                "code": 105,
                "type": "https_access_restricted",
                "info": "Access Restricted - Your current Subscription Plan does not support HTTPS Encryption."
            }
        })
        mock_requests.get.return_value = mock_response

        # Run function should raise error because API returns error field in response
        self.assertRaises(ServiceResponseError, lambda: get_current_weather(30076))

        # Check if call request get with correct parameters
        mock_requests.get.assert_called_with(API_URI.format(ACCESS_TOKEN, 30076))

    @patch('app.api.requests')
    def test_request_api_error_with_current_field_not_in_the_response(self, mock_requests):
        # Setup requests mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "request": {
                "type": "Zipcode",
                "query": "30076",
                "language": "en",
                "unit": "m"
            },
            "location": {
                "name": "Roswell",
                "country": "USA",
                "region": "Georgia",
                "lat": "34.026",
                "lon": "-84.312",
                "timezone_id": "America\/New_York",
                "localtime": "2023-04-06 10:39",
                "localtime_epoch": 1680777540,
                "utc_offset": "-4.0"
            }
        })
        mock_requests.get.return_value = mock_response

        # Run function should raise error because API returns no current data field
        self.assertRaises(DataNotContainedResponseError, lambda: get_current_weather(30076))

        # Check if call request get with correct parameters
        mock_requests.get.assert_called_with(API_URI.format(ACCESS_TOKEN, 30076))

    @patch('app.api.requests')
    def test_request_api_error_with_current_field_in_the_response_but_contains_malformed_data(self, mock_requests):
        # Setup requests mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "request": {
                "type": "Zipcode",
                "query": "30076",
                "language": "en",
                "unit": "m"
            },
            "location": {
                "name": "Roswell",
                "country": "USA",
                "region": "Georgia",
                "lat": "34.026",
                "lon": "-84.312",
                "timezone_id": "America\/New_York",
                "localtime": "2023-04-06 10:39",
                "localtime_epoch": 1680777540,
                "utc_offset": "-4.0"
            },
            "current": {
                "observation_time": "02:39 PM",
                "temperature": 22,
                "weather_code": "This is invalid value",
                "weather_icons": [
                    "https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0002_sunny_intervals.png"
                ],
                "weather_descriptions": ["Partly cloudy"],
                "wind_speed": 4,
                "wind_degree": 253,
                "wind_dir": "WSW",
                "pressure": 1024,
                "precip": 0,
                "humidity": 81,
                "cloudcover": 75,
                "feelslike": 22,
                "uv_index": 6,
                "visibility": 16,
                "is_day": "yes"
            }
        })
        mock_requests.get.return_value = mock_response

        # Run function should raise error because API returns weather data with invalid content
        self.assertRaises(MalformedDataResponseError, lambda: get_current_weather(30076))

        # Check if call request get with correct parameters
        mock_requests.get.assert_called_with(API_URI.format(ACCESS_TOKEN, 30076))


if __name__ == '__main__':
    unittest.main()
