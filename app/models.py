from .utils import get_number


class WeatherInfo(object):
    """
    This object contains weather information
    """

    def __init__(
            self,
            weather_code: float,
            wind_speed: float,
            uv_index: float,
            temperature: float,
            humidity: float
    ):
        """
        :param weather_code: the code of weather from Weather Stack. Ref: https://weatherstack.com/documentation
        :param wind_speed: the current speed of wind
        :param uv_index: the current UV index
        :param temperature: the current temperature in Celsius degree
        :param humidity: the current humidity in percentage
        """
        self.weather_code = weather_code
        self.wind_speed = wind_speed
        self.uv_index = uv_index
        self.temperature = temperature
        self.humidity = humidity

    @staticmethod
    def from_data(data: dict):
        return WeatherInfo(
            get_number(data, 'weather_code'),
            get_number(data, 'wind_speed'),
            get_number(data, 'uv_index'),
            get_number(data, 'temperature'),
            get_number(data, 'humidity'),
        )
