import os
import json
import requests

from utils.enum import Region
from utils.exception import *
from .updater import WotApiUpdater


class WoTAPI:

    def __init__(self, api_token: str, region=Region.ASIA, folder=os.getcwd()):
        # Definition Constant
        self.API_TOKEN = api_token
        self.REGION = region
        self.MAIN_URL = region.value
        self.ACCOUNT_URL = f"{self.MAIN_URL}/account"
        self.CLANS_URL = f"{self.MAIN_URL}/clans"
        self.GMAP_URL = f"{self.MAIN_URL}/globalmap"
        # Initialize API Updater
        self.updater = WotApiUpdater(folder)
        self.updater.update()
