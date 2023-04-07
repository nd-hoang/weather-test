from .models import WeatherInfo
from .config import SHOULD_NOT_GO_OUTSIDE_WEATHER_CODE
from .config import SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX
from .config import CAN_FLY_KITE_IF_WIND_SPEED_OVER


def is_rain(weather_info: WeatherInfo) -> bool:
    """
    Yes if it has weather_code contains "rain" word
    """
    return weather_info.weather_code in SHOULD_NOT_GO_OUTSIDE_WEATHER_CODE


def should_go_outside(weather_info: WeatherInfo) -> bool:
    """
    Yes if it is not raining
    """
    return not is_rain(weather_info)


def should_wear_sunscreen(weather_info: WeatherInfo) -> bool:
    """
    Yes if UV index above SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX param
    """
    return weather_info.uv_index > SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX


def can_fly_kite(weather_info: WeatherInfo) -> bool:
    """
    Yes if not raining and wind speed over CAN_FLY_KITE_IF_WIND_SPEED_OVER param
    """
    return not is_rain(weather_info) and weather_info.wind_speed > CAN_FLY_KITE_IF_WIND_SPEED_OVER
