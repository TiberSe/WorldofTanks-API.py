import os
import json
import requests
import re

from .utils.enum import Region
from .utils.exception import *
from .updater import WotApiUpdater


class WoTAPI:

    def __init__(self, api_token: str, region=Region.ASIA, lang='en', folder=os.getcwd()):
        # Definition Constant
        self._API_TOKEN = api_token
        self._REGION = region
        self._LOCAL_LANG = lang
        self._API_LANG = 'en'  # TODO: 'en'はru地域ではサポートされてないからregionがruのときだけ言語もruにするコードをいつか書く。
        self._MAIN_URL = region.value
        self._ACCOUNT_URL = f'{self._MAIN_URL}/account'
        self._CLANS_URL = f'{self._MAIN_URL}/clans'
        self._GMAP_URL = f'{self._MAIN_URL}/globalmap'
        # Initialize API Updater
        self._updater = WotApiUpdater(folder)
        self._updater.update()

    def get_account_info_by_id(self, account_id: int, extra: str = '', fields: tuple = ()) -> dict:
        if not isinstance(account_id, int):
            raise IllegalTypeException(var_name='account_id', contents=account_id, intend='Integer')
        fields = self.parse_tuple(fields)
        response = requests.get(f'{self._ACCOUNT_URL}/info/?application_id={self._API_TOKEN}&account_id={account_id}&'
                                f'&fields={fields}&extra={extra}&language={self._API_LANG}')
        account_data = json.loads(response.text)
        return account_data

    def get_account_id_by_name(self, account_name: str, limit: int = 5, exact: bool = True, fields: tuple = ()) -> dict:
        if not isinstance(account_name, str):
            raise IllegalTypeException(var_name='account_name', value=account_name, intend='longer than 3 chars')
        if not isinstance(limit, int):
            raise IllegalTypeException(var_name='limit', value=limit, intend='Integer')
        fields = self.parse_tuple(fields)
        exact = 'exact' if exact else 'startswith'
        response = requests.get(f'{self._ACCOUNT_URL}/list/?application_id={self._API_TOKEN}&search={account_name}&'
                                f'type={exact}&fields={fields}&language={self._API_LANG}')
        account_data = json.loads(response.text)
        return account_data

    @staticmethod
    def parse_tuple(data: tuple) -> str:
        data = re.sub("\(|\'|\)|\ ", '', str(data))
        return data
