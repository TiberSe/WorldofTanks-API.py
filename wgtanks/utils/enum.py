from enum import Enum


class Region(Enum):
    ASIA = 'https://api.worldoftanks.asia/wot'
    NA = 'https://api.worldoftanks.com/wot'
    EU = 'https://api.worldoftanks.eu/wot'
    RU = 'https://api.worldoftanks.ru/wot'


class Lang(Enum):
    EN = 'en'
    RU = 'ru'
