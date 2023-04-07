import re

# Precompile the regex for match only lowercase alphabets and numbers
handled_characters_re = re.compile(r'[^a-z0-9]+')
us_zipcode_re = re.compile(r'.*(\d{5}(\-\d{4})?)$')


def get_number(data: dict, key: str) -> float:
    """
    Utility function for get integer value from a dictionary

    :param data: Dictionary to get value
    :param key: Key of attribute to get value
    :return: Value of the key in data as number
    """
    if key not in data:
        raise ValueError(f'"{key}" does not exist in data')
    try:
        return float(data[key])
    except ValueError:
        raise ValueError(f'"{key}" is not a number. Value: {data[key]}')


def preprocess_input(input_str: str) -> str:
    """
    Utility function for preprocess question string for matching improvement

    :param input_str: Original question
    :return: The question convert to lowercase and only accept alphabets and numbers
    """
    return handled_characters_re.sub('', input_str.lower().strip())


def is_us_zipcode(zip_code: int) -> bool:
    """
    US zip code range from 00501 to 99950
    :param zip_code: Zip code to check
    :return: True if the input code in the valid range
    """
    return 501 <= zip_code <= 99950
