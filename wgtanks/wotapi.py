import inspect
import os
import json
import requests


from .utils.enum import Region
from .utils.exception import *
from .updater import WotApiUpdater
from .utils.except_params import params as except_params


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
        self._params = except_params

    def get_account_id_by_name(self, account_name: str, limit: int = 5, exact: bool = True, fields: tuple = ()) -> dict:
        """Find and retrieves the account ID by account name.

        :param str account_name: The name of the account to lookup. (Min: 3 chars, Max: 24 chars)
        :param int limit: The maximum number of results to return. (Min: 1, Max: 100)
        :param bool exact: Whether to return only results that match the exact string. (Default: True)
        :param tuple fields: A tuple of fields to return in the results.

        :return: dict containing the account ID
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        exact = 'exact' if exact else 'startswith'
        url = f"{self._ACCOUNT_URL}/list/?application_id={self._API_TOKEN}&language={self._API_LANG}&type={exact}&"\
              'search={account_name}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_account_info_by_id(self, account_id: tuple, extra: str = '', fields: tuple = ()) -> dict:
        """Retrieves the account info by account ID.

        :param tuple account_id: A tuple or int of ID(s) for the accounts to lookup. (Max: 100)
        :param tuple extra: A tuple of extra fields.
        :param tuple fields: A tuple of fields to return in the results.

        :return: dict containing the account info.
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f"{self._ACCOUNT_URL}/info/?application_id={self._API_TOKEN}&language={self._API_LANG}&"\
              '&account_id={account_id}&extra={extra}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_players_vehicles(self, account_id: tuple, tank_id: tuple = (), fields: tuple = ()) -> dict:
        """Find and retrieves the account ID by account name.

        :param int account_id: A tuple or int of ID(s) for the account to lookup. (Max: 100)
        :param tuple tank_id: A tuple or int of tank(s) ID to retrieves. (Max: 100)
        :param tuple fields: A tuple or string of field(s) to return in the results. (Max: 100)

        :return: dict containing the player's tanks info
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._ACCOUNT_URL}/tanks/?application_id={self._API_TOKEN}&language={self._API_LANG}&'\
              'account_id={account_id}&tank_id={tank_id}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_players_achievements(self, account_id: tuple, fields: tuple = ()) -> dict:
        """Find and retrieves the player's achievements by account ID.

        :param int account_id: The tuple or int of ID(s) to the account(s) to lookup. (Max: 100)
        :param tuple fields: A tuple of fields to return in the results. (Max: 100)

        :return: dict containing the player's tanks info
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._ACCOUNT_URL}/achievements/?application_id={self._API_TOKEN}&language={self._API_LANG}&'\
              'account_id={account_id}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_clan_info_by_name(self, clan_name: str, limit: int = 5, page_no: int = 1, fields: tuple = ()) -> dict:
        """Find and retrieves the clan info by clan name or clan tag.

        :param str clan_name: The name of the account to lookup. (Min: 3 chars, Max: 24 chars)
        :param int limit: The maximum number of results to return. (Min: 1, Max: 100)
        :param int page_no: Page number of the search result to be acquired. (Min: 1, Max: 100)
        :param tuple fields: A tuple of fields to return in the results. (Max: 100)

        :return: dict containing the clan info
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._CLANS_URL}/list/?application_id={self._API_TOKEN}&language={self._API_LANG}&'\
              'search={clan_name}&page_no={page_no}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def __fix_params(self, args: dict):
        for param in self._params[inspect.stack()[1].function]:
            if param['name'] in args:
                if 'incl_only' not in param:
                    continue
                var = args[param['name']]
                if not isinstance(var, param['type']) and isinstance(var, param['incl_only']):
                    fixed_var = [var]
                    fixed_var = tuple(map(param['incl_only'], fixed_var))
                    args[param['name']] = fixed_var
        return args

    @staticmethod
    def __parse_tuple(args: dict) -> dict:
        for arg in args.items():
            if isinstance(arg[1], tuple):
                args[arg[0]] = ','.join(map(str, arg[1]))
        return args

    def __integrity_check(self, args: dict):
        for param in self._params[inspect.stack()[1].function]:
            param['value'] = args[param['name']]
            if 'type' in param:
                if not isinstance(param['value'], param['type']):
                    raise IllegalTypeException(
                        var_name=param['name'], value=param['value'], intend=str(param['type']))
            if 'min_len' in param:
                if not len(param['value']) >= param['min_len']:
                    raise IllegalLengthException(
                        var_name=param['name'], value=param['value'], intend=f'longer than {param["min_len"]} chars')
            if 'max_len' in param:
                if not len(param['value']) <= param['max_len']:
                    raise IllegalLengthException(
                        var_name=param['name'], value=param['value'], intend=f'less than {param["max_len"]} chars')
            if 'min_num' in param:
                if not param['value'] >= param['min_num']:
                    raise IllegalLengthException(
                        var_name=param['name'], value=param['value'], intend=f'more than {param["min_num"]}')
            if 'max_num' in param:
                if not param['value'] <= param['max_num']:
                    raise IllegalLengthException(
                        var_name=param['name'], value=param['value'], intend=f'less than {param["max_num"]}')
            if 'incl_only' in param:
                for series in param['value']:
                    if not isinstance(series, param['incl_only']):
                        raise IllegalTypeException(
                            var_name=param['name'], value=param['value'], intend=str(param['incl_only']))
            param['value'] = None
        return
