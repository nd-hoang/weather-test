import unittest
from app.config import SHOULD_NOT_GO_OUTSIDE_WEATHER_CODE
from app.config import SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX
from app.config import CAN_FLY_KITE_IF_WIND_SPEED_OVER
from app.models import WeatherInfo
from app.services import is_rain
from app.services import should_go_outside
from app.services import should_wear_sunscreen
from app.services import can_fly_kite


# Rain weather codes
# 176,  # Patchy rain possible
# 293,  # Patchy light rain
# 296,  # Light rain
# 299,  # Moderate rain at times
# 302,  # Moderate rain
# 305,  # Heavy rain at times
# 308,  # Heavy rain
# 311,  # Light freezing rain


class TestServices(unittest.TestCase):
    def test_is_raining(self):
        # Run function
        # Check if weather code is in rain weather codes
        for code in SHOULD_NOT_GO_OUTSIDE_WEATHER_CODE:
            self.assertEqual(is_rain(WeatherInfo(code, 0, 0, 0, 0)), True)

    def test_is_not_raining(self):
        # Run function
        # Check if weather code is not in rain weather codes
        self.assertEqual(is_rain(WeatherInfo(333, 0, 0, 0, 0)), False)
        self.assertEqual(is_rain(WeatherInfo(-1, 0, 0, 0, 0)), False)
        self.assertEqual(is_rain(WeatherInfo(0, 0, 0, 0, 0)), False)

    def test_should_go_outside_if_not_raining(self):
        # Run function
        # Set weather code is not in rain weather codes for not raining
        self.assertEqual(should_go_outside(WeatherInfo(999, 0, 0, 0, 0)), True)
        self.assertEqual(should_go_outside(WeatherInfo(-1, 0, 0, 0, 0)), True)
        self.assertEqual(should_go_outside(WeatherInfo(0, 0, 0, 0, 0)), True)

    def test_should_not_go_outside_if_raining(self):
        # Run function
        # Set weather code is in rain weather codes for raining
        for code in SHOULD_NOT_GO_OUTSIDE_WEATHER_CODE:
            self.assertEqual(should_go_outside(WeatherInfo(code, 0, 0, 0, 0)), False)

    def test_should_wear_sunscreen_if_uv_index_over_threshold(self):
        base_value = SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX
        # Run function
        # Set weather code is not in rain weather codes for not raining
        self.assertEqual(should_wear_sunscreen(WeatherInfo(0, 0, base_value + 0.00000001, 0, 0)), True)
        self.assertEqual(should_wear_sunscreen(WeatherInfo(0, 0, base_value + 0.1, 0, 0)), True)
        self.assertEqual(should_wear_sunscreen(WeatherInfo(0, 0, base_value + 1000, 0, 0)), True)

    def test_should_not_wear_sunscreen_if_uv_index_not_over_threshold(self):
        base_value = SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX
        # Run function
        # Set weather code is not in rain weather codes for not raining
        self.assertEqual(should_wear_sunscreen(WeatherInfo(0, 0, base_value, 0, 0)), False)
        self.assertEqual(should_wear_sunscreen(WeatherInfo(0, 0, base_value - 0.00000001, 0, 0)), False)
        self.assertEqual(should_wear_sunscreen(WeatherInfo(0, 0, base_value - 9999, 0, 0)), False)

    def test_can_fly_sky_if_not_rain_and_wind_speed_over_threshold(self):
        base_value = CAN_FLY_KITE_IF_WIND_SPEED_OVER
        # Run function
        # Set weather code is not in rain weather codes for not raining
        self.assertEqual(can_fly_kite(WeatherInfo(333, base_value + 0.00000001, 0, 0, 0)), True)
        self.assertEqual(can_fly_kite(WeatherInfo(333, base_value + 0.1, 0, 0, 0)), True)
        self.assertEqual(can_fly_kite(WeatherInfo(333, base_value + 1000, 0, 0, 0)), True)

    def test_can_not_fly_sky_if_not_rain_and_wind_speed_not_over_threshold(self):
        base_value = CAN_FLY_KITE_IF_WIND_SPEED_OVER
        # Run function
        # Set weather code is not in rain weather codes for not raining
        self.assertEqual(can_fly_kite(WeatherInfo(333, base_value, 0, 0, 0)), False)
        self.assertEqual(can_fly_kite(WeatherInfo(333, base_value - 0.00000001, 0, 0, 0)), False)
        self.assertEqual(can_fly_kite(WeatherInfo(333, base_value - 9999, 0, 0, 0)), False)

    def test_can_not_fly_sky_if_wind_speed_over_threshold_but_raining(self):
        base_value = CAN_FLY_KITE_IF_WIND_SPEED_OVER
        # Run function
        # Set weather code is not in rain weather codes for not raining
        self.assertEqual(can_fly_kite(WeatherInfo(308, base_value + 0.00000001, 0, 0, 0)), False)
        self.assertEqual(can_fly_kite(WeatherInfo(308, base_value + 0.1, 0, 0, 0)), False)
        self.assertEqual(can_fly_kite(WeatherInfo(308, base_value + 1000, 0, 0, 0)), False)


if __name__ == '__main__':
    unittest.main()
