from .extends_escapes import Colors, Escapes


class WotApiException(Exception):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    pass


class IllegalTypeException(WotApiException):
    def __str__(self):
        return (
            f"The type of variable: {Escapes.REVERSE}{self.kwargs['var_name']}{Escapes.RESET} must be "
            f"{self.kwargs['intend']}.\n Please assign the correct value. Value: \"{self.kwargs['value']}\""
        )


class IllegalLengthException(WotApiException):
    def __str__(self):
        return (
            f"The length of variable: {Escapes.REVERSE}{self.kwargs['var_name']}{Escapes.RESET} must be "
            f"{self.kwargs['intend']}.\n Please assign the correct value.\n Value: \"{self.kwargs['value']}\""
        )
