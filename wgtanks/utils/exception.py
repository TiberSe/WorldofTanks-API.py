class WotApiException(Exception):
    def __init__(self, arg=""):
        self.arg = arg
    pass


class IllegalTypeException(WotApiException):
    def __str__(self):
        return (
            f"\033[31m The type of variable :{self.arg} is illegal. Please assign the correct value.`"
        )
    pass


class UnknownLanguageException(WotApiException):
    pass


class UnknownChapterException(WotApiException):
    pass


class UnknownDifficultyException(WotApiException):
    pass


class UnknownMemoryException(WotApiException):
    pass


class UnknownFactionException(WotApiException):
    pass


class UnknownEquipmentException(WotApiException):
    pass
