import unittest
from app.models import WeatherInfo


class TestModels(unittest.TestCase):
    def test_construct_weather_info_successfully(self):
        test_value = {
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

        # Run function
        actual = WeatherInfo.from_data(test_value)

        # Check if result is not None
        self.assertIsNotNone(actual)
        # Check if result has correct values
        self.assertEqual(actual.weather_code, 116)
        self.assertEqual(actual.wind_speed, 4)
        self.assertEqual(actual.uv_index, 6)
        self.assertEqual(actual.temperature, 22)
        self.assertEqual(actual.humidity, 81)

    def test_error_raised_if_any_required_field_is_missing(self):
        test_value = {
            "observation_time": "02:39 PM",
            "temperature": 22,
            "weather_code": 116,
            "weather_icons": [
                "https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0002_sunny_intervals.png"
            ],
            "weather_descriptions": ["Partly cloudy"],
            # "wind_speed": 4,
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

        # Check exception raised if value of field does not exist
        self.assertRaises(ValueError, lambda: WeatherInfo.from_data(test_value))

    def test_error_raised_if_all_required_fields_are_missing(self):
        test_value = {
            "observation_time": "02:39 PM",
            # "temperature": 22,
            # "weather_code": 116,
            "weather_icons": [
                "https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0002_sunny_intervals.png"
            ],
            "weather_descriptions": ["Partly cloudy"],
            # "wind_speed": 4,
            "wind_degree": 253,
            "wind_dir": "WSW",
            "pressure": 1024,
            "precip": 0,
            # "humidity": 81,
            "cloudcover": 75,
            "feelslike": 22,
            # "uv_index": 6,
            "visibility": 16,
            "is_day": "yes"
        }

        # Check exception raised if value of field does not exist
        self.assertRaises(ValueError, lambda: WeatherInfo.from_data(test_value))

    def test_error_raised_if_any_required_field_contains_invalid_value(self):
        test_value = {
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
            "uv_index": "THIS SHOULD BE A NUMBER",
            "visibility": 16,
            "is_day": "yes"
        }

        # Check exception raised if value of field does not exist
        self.assertRaises(ValueError, lambda: WeatherInfo.from_data(test_value))

    def test_error_raised_if_all_required_fields_contains_invalid_value(self):
        test_value = {
            "observation_time": "02:39 PM",
            "temperature": "THIS SHOULD BE A NUMBER",
            "weather_code": "THIS SHOULD BE A NUMBER",
            "weather_icons": [
                "https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0002_sunny_intervals.png"
            ],
            "weather_descriptions": ["Partly cloudy"],
            "wind_speed": "THIS SHOULD BE A NUMBER",
            "wind_degree": 253,
            "wind_dir": "WSW",
            "pressure": 1024,
            "precip": 0,
            "humidity": "THIS SHOULD BE A NUMBER",
            "cloudcover": 75,
            "feelslike": 22,
            "uv_index": "THIS SHOULD BE A NUMBER",
            "visibility": 16,
            "is_day": "yes"
        }

        # Check exception raised if value of field does not exist
        self.assertRaises(ValueError, lambda: WeatherInfo.from_data(test_value))


if __name__ == '__main__':
    unittest.main()
