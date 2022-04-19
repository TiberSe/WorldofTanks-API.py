import inspect
import os
import json
import requests

from .utils import except_params
from .utils import warehouse
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
        self._CLANRATINGS_URL = f'{self._MAIN_URL}/clanratings'
        # Initialize API Updater
        self._updater = WotApiUpdater(folder)
        self._updater.update()
        self._params = except_params.params

    @staticmethod
    def print_api_wrapper_logo(sheffield=False):
        """Prints the logo of this wrapper.
        """
        if sheffield:
            print(warehouse.sheffield)
            return True
        print(warehouse.api_logo)
        return True

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

    def get_account_info(self, account_id: tuple, extra: str = '', fields: tuple = ()) -> dict:
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
        """Find and retrieves clans info by clan name or clan tag.

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

    def get_clan_member_details(self, account_id: tuple, fields: tuple = ()) -> dict:
        """Find and retrieves the clan member info by account id.

        :param int account_id: A tuple or int of ID(s) to clan lookup. (Min: 1, Max: 100)
        :param tuple fields: A tuple of fields to return in the results. (Max: 100)

        :return: dict containing the clan member details
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._CLANS_URL}/accountinfo/?application_id={self._API_TOKEN}&language={self._API_LANG}&'\
              'account_id={account_id}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_clan_glossary(self, fields: tuple = ()) -> dict:
        """Retrieves the clan glossary.

        :param tuple fields: A tuple of fields to return in the results. (Max: 100)

        :return: dict containing the clan glossary.
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._CLANS_URL}/glossary/?application_id={self._API_TOKEN}&language={self._API_LANG}&' \
              'fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_clan_messageboard(self, access_token, fields: tuple = ()) -> dict:
        """Find and retrieves the clan member info by account id.

        :param str access_token: A string of access token to access private information. (Max: 100)
        :param tuple fields: A tuple of fields to return in the results. (Max: 100)

        :return: dict containing the clan glossary
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._CLANS_URL}/messageboard/?application_id={self._API_TOKEN}&language={self._API_LANG}&' \
              'access_token={access_token}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_players_clan_history(self, account_id: int, fields: tuple = ()) -> dict:
        """Find and retrieves the clan member info by account id.

        :param int account_id: The int of ID to the account to lookup. (Max: 1)
        :param tuple fields: A tuple of fields to return in the results. (Max: 100)

        :return: dict containing the player's clan history
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._CLANS_URL}/memberhistory/?application_id={self._API_TOKEN}&language={self._API_LANG}&' \
              'account_id={account_id}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_types_of_clan_ratings(self):
        """Retrieves types of ratings.

        :return: dict containing the player's clan history
        """
        url = f'{self._CLANRATINGS_URL}/types/?application_id={self._API_TOKEN}'
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_dates_with_available_clan_ratings(self, limit: int = 7):
        """Retrieves types of ratings.

        :param int limit: The int of Limit to the dates with available ratings to lookup. (Max: 365)

        :return: dict containing the player's clan history
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f'{self._CLANRATINGS_URL}/dates/?application_id={self._API_TOKEN}' \
              '&limit={limit}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_clan_ratings(self, clan_id: tuple, fields: tuple = ()) -> dict:
        """Retrieves the clan ratings info by clan ID.

        :param tuple clan_id: A tuple or int of ID(s) for the clan ratings to lookup. (Max: 100)
        :param tuple fields: A tuple of fields to return in the results.

        :return: dict containing the account info.
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f"{self._CLANRATINGS_URL}/clans/?application_id={self._API_TOKEN}&language={self._API_LANG}&"\
              '&clan_id={clan_id}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_clan_adjacent_position_in_rating(self, clan_id: int, rank_field: str, date: int, limit: int = 5, fields: tuple = ()):
        """Retrieves the clan neighbors in ratings by clan ID.

        :param int clan_id: The int of ID for the clan ratings to lookup. (Max: 1)
        :param str rank_field: The string of rank field to lookup.
        :param int date: The int of date for the clan ratings to lookup.
        :param int limit: The int of Limit to the dates with available ratings to lookup. (Max: 50)
        :param tuple fields: A tuple of fields to return in the results.

        :return: dict containing the clan rating position neighbors.
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f"{self._CLANRATINGS_URL}/neighbors/?application_id={self._API_TOKEN}&language={self._API_LANG}&" \
              '&rank_field={rank_field}&date={date}&limit={limit}&fields={fields}'.format(**args)
        response = requests.get(url)
        return_data = json.loads(response.text)
        return return_data

    def get_ratings_top_clans(self, rank_field: str, date: int, limit: int = 10, page_no: int = 1, fields: tuple = ()):
        """Retrieves the top clans in ratings by ranking field.

        :param str rank_field: The string of rank field to lookup.
        :param int date: The int of date for the clan ratings to lookup.
        :param int limit: The int of Limit to the dates with available ratings to lookup. (Max: 50)
        :param int page_no: The int of page number to retrieve. (Max: 10)
        :param tuple fields: A tuple of fields to return in the results.

        :return: dict containing the clan rating top clans.
        """
        args = locals()
        args = self.__fix_params(args)
        self.__integrity_check(args)
        args = self.__parse_tuple(args)
        url = f"{self._CLANRATINGS_URL}/top/?application_id={self._API_TOKEN}&language={self._API_LANG}&" \
              '&rank_field={rank_field}&date={date}&limit={limit}&page_no={page_no}&fields={fields}'.format(**args)
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
                    fixed_var = tuple(map(param['incl_only'], [var]))
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
