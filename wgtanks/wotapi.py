import os
import json
import requests

from .utils.enum import Region
from .utils.exception import *
from .updater import WotApiUpdater


class WoTAPI:

    def __init__(self, api_token: str, region=Region.ASIA, lang="ja", folder=os.getcwd()):
        # Definition Constant
        self._API_TOKEN = api_token
        self._REGION = region
        self._LANG = lang
        self._MAIN_URL = region.value
        self._ACCOUNT_URL = f"{self._MAIN_URL}/account"
        self._CLANS_URL = f"{self._MAIN_URL}/clans"
        self._GMAP_URL = f"{self._MAIN_URL}/globalmap"
        # Initialize API Updater
        self._updater = WotApiUpdater(folder)
        self._updater.update()

    def get_account_by_id(self, account_id: int, **kwargs) -> dict:
        if not isinstance(account_id, int):
            raise IllegalTypeException(account_id)
            return False
        request_url = f"{self._ACCOUNT_URL}/info/?application_id={self._API_TOKEN}"
        response = requests.get(f'{self._ACCOUNT_URL}/info/?application_id={self._API_TOKEN}&account_id={account_id}')
        account_data = json.loads(response.text)
        return account_data
