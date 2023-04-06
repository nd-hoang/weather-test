ACCESS_TOKEN = '610acf4c1d203448cd6f671955c5e8aa'

QUESTIONS = [
    "Should I go outside?",
    "Should I wear sunscreen?",
    "Can I fly my kite?"
]

# Weather code table can get from https://weatherstack.com/documentation
# Current I select all codes which related to rain
SHOULD_NOT_GO_OUTSIDE_WEATHER_CODE = [
    176,    # Patchy rain possible
    293,    # Patchy light rain
    296,    # Light rain
    299,    # Moderate rain at times
    302,    # Moderate rain
    305,    # Heavy rain at times
    308,    # Heavy rain
    311,    # Light freezing rain
]

SHOULD_WEAR_SUNSCREEN_IF_ABOVE_UV_INDEX = 3

CAN_FLY_KITE_IF_WIND_SPEED_OVER = 15
