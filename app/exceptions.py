class APIRequestError(Exception):
    """
    Base API Request Error
    """

    def __init__(self, *args: object) -> None:
        super().__init__(args)


class ConnectionResponseError(APIRequestError):
    """
    Occurs if request get any connection error: Timeout, DNS, Refused, Too Many Redirects
    """
    def __init__(self, *args: object) -> None:
        super().__init__(args)


class HttpCodeResponseError(APIRequestError):
    """
    Occurs if status HTTP code is not 200
    """
    def __init__(self, *args: object) -> None:
        super().__init__(args)


class InvalidJsonResponseError(APIRequestError):
    """
    Occurs if response is not in JSON format
    """
    def __init__(self, *args: object) -> None:
        super().__init__(args)


class ServiceResponseError(APIRequestError):
    """
    Occurs if response contains the "error" field
    """
    def __init__(self, *args: object) -> None:
        super().__init__(args)


class DataNotContainedResponseError(APIRequestError):
    """
    Occurs if response does not contain the "current" field which is weather data
    """
    def __init__(self, *args: object) -> None:
        super().__init__(args)


class MalformedDataResponseError(APIRequestError):
    """
    Occurs if weather data does not contain required fields, or these fields has invalid value
    """
    def __init__(self, *args: object) -> None:
        super().__init__(args)
