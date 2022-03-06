import inspect
import os
import json
import requests
import re
import time

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
        """Retrieves the account info by account ID.

        :param tuple account_id: a tuple or int of ID(s) for the accounts to lookup. (Max: 100)
        :param str extra: extra field.
        :param tuple fields: a tuple of fields to return in the results.

        :return: dict containing the account info.
        """
        print(inspect.stack()[1].function)
        if isinstance(account_id, int):
            params = [
                {'name': 'account_id', 'value': account_id, 'type': int},
                {'name': 'extra', 'value': extra, 'type': str}, {'name': 'fields', 'value': fields, 'type': tuple}
            ]
        else:
            params = [
                {'name': 'account_id', 'value': account_id, 'type': tuple, 'incl_only': int, 'min_len': 1,
                 'max_len': 100},
                {'name': 'extra', 'value': extra, 'type': str}, {'name': 'fields', 'value': fields, 'type': tuple}
            ]

        self.__integrity_check(params)
        fields = self.__parse_tuple(fields)
        response = requests.get(f'{self._ACCOUNT_URL}/info/?application_id={self._API_TOKEN}&account_id={account_id}&'
                                f'&fields={fields}&extra={extra}&language={self._API_LANG}')
        account_data = json.loads(response.text)
        return account_data

    def get_account_id_by_name(self, account_name: str, limit: int = 5, exact: bool = True, fields: tuple = ()) -> dict:
        """Find and retrieves the account ID by account name.

        :param str account_name: the name of the account to lookup. (Min: 3 chars, Max: 24 chars)
        :param int limit: the maximum number of results to return. (Min: 1, Max: 100)
        :param bool exact: whether to return only results that match the exact string. (Default: True)
        :param tuple fields: a tuple of fields to return in the results.

        :return: dict containing the account ID
        """
        params = [
            {'name': 'account_name', 'value': account_name, 'type': str, 'min_len': 3, 'max_len': 24},
            {'name': 'limit', 'value': limit, 'type': int, 'min_num': 1, 'max_num': 100},
            {'name': 'exact', 'value': exact, 'type': bool},
            {'name': 'fields', 'value': fields, 'type': tuple}
        ]
        self.__integrity_check(params)
        fields = self.__parse_tuple(fields)
        exact = 'exact' if exact else 'startswith'
        response = requests.get(f'{self._ACCOUNT_URL}/list/?application_id={self._API_TOKEN}&search={account_name}&'
                                f'type={exact}&fields={fields}&language={self._API_LANG}')
        account_data = json.loads(response.text)
        return account_data

    def get_players_vehicles(self, account_id: int, tank_id: tuple = (), fields: tuple = ()) -> dict:
        """Find and retrieves the account ID by account name.

        :param int account_id: the id of the account to lookup.
        :param tuple tank_id: a tuple of tanks ID to retrieves (Max: 100)
        :param tuple fields: a tuple of fields to return in the results.

        :return: dict containing the player's tanks info
        """
        params = [
            {'name': 'account_id', 'value': account_id, 'type': int, 'min_num': 0, 'max_num': 9000000000},
            {'name': 'tank_id', 'value': tank_id, 'type': tuple, 'min_len': 0, 'max_len': 100},
            {'name': 'fields', 'value': fields, 'type': tuple}
        ]
        self.__integrity_check(params)
        fields = self.__parse_tuple(fields)
        tank_id = self .__parse_tuple(tank_id)
        response = requests.get(f'{self._ACCOUNT_URL}/tanks/?application_id={self._API_TOKEN}&account_id={account_id}&'
                                f'tank_id={tank_id}&fields={fields}&language={self._API_LANG}')
        account_data = json.loads(response.text)
        return account_data

    def get_players_achievements(self, account_id: int, fields: tuple = ()) -> dict:
        """Find and retrieves the player's achievements by account ID.

        :param int account_id: the id of the account to lookup.
        :param tuple fields: a tuple of fields to return in the results.

        :return: dict containing the player's tanks info
        """
        params = [
            {'name': 'account_id', 'value': account_id, 'type': int, 'min_num': 0, 'max_num': 9000000000},
            {'name': 'fields', 'value': fields, 'type': tuple}
        ]
        self.__integrity_check(params)
        fields = self.__parse_tuple(fields)
        response = requests.get(f'{self._ACCOUNT_URL}/achievements/?application_id={self._API_TOKEN}&'
                                f'account_id={account_id}&fields={fields}&language={self._API_LANG}')
        account_data = json.loads(response.text)
        return account_data

    @staticmethod
    def __parse_tuple(data: tuple) -> str:
        data = re.sub("\(|\'|\)|\ ", '', str(data))
        return data

    @staticmethod
    def __integrity_check(params: list):
        for prm in params:
            if 'type' in prm:
                if not isinstance(prm['value'], prm['type']):
                    raise IllegalTypeException(var_name=prm['name'], value=prm['value'], intend=str(prm['type']))
            if 'min_len' in prm:
                if not len(prm['value']) >= prm['min_len']:
                    raise IllegalLengthException(
                        var_name=prm['name'], value=prm['value'], intend=f'longer than {prm["min_len"]} chars')
            if 'max_len' in prm:
                if not len(prm['value']) <= prm['max_len']:
                    raise IllegalLengthException(
                        var_name=prm['name'], value=prm['value'], intend=f'less than {prm["max_len"]} chars')
            if 'min_num' in prm:
                if not prm['value'] >= prm['min_num']:
                    raise IllegalLengthException(
                        var_name=prm['name'], value=prm['value'], intend=f'more than {prm["min_num"]}')
            if 'max_num' in prm:
                if not prm['value'] <= prm['max_num']:
                    raise IllegalLengthException(
                        var_name=prm['name'], value=prm['value'], intend=f'less than {prm["max_num"]}')
            if 'incl_only' in prm:
                for series in prm['value']:
                    if not isinstance(series, prm['incl_only']):
                        raise IllegalTypeException(
                            var_name=prm['name'], value=prm['value'], intend=str(prm['incl_only']))

        return
