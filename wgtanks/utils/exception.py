from .extends_escapes import Colors, Escapes


class WotApiException(Exception):
    def __init__(self, arg=""):
        self.arg = arg
    pass


class IllegalTypeException(WotApiException):
    def __str__(self):
        return (
            f"The type of variable: {Escapes.REVERSE + Escapes.BOLD}account_id{Escapes.RESET} is illegal. "
            f"Please assign the correct value.\nContents: {self.arg}"
        )
    pass


class UnknownLanguageException(WotApiException):
    pass
