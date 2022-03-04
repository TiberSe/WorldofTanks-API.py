import os
import json
import requests

# Constantinopolis
CDN_URL = 'https://raw.githubusercontent.com/TiberSe/wgapi-cdn/main/wot/'
EXCEPT_PARAMS = f'{CDN_URL}/params/except.json'
TANK_LIST = f'{CDN_URL}/tanks/list.json'


class WotApiUpdater:

    def __init__(self, folder):
        self.current_dir = folder
        self.data_folder = f"{self.current_dir}{os.sep}wotapi_data"
        if not os.path.exists(self.data_folder):
            os.mkdir(self.data_folder)

        self.ships_file = f"{self.data_folder}{os.sep}tanks.json"
        self.files = [self.ships_file]

    def update(self):
        pass

