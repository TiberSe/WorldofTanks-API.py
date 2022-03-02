import os
import json
import requests

from .updater import WotApiUpdater


class WoTAPI:

    def __init__(self, folder=os.getcwd()):
        self.updater = WotApiUpdater(folder)
        self.updater.update()
        

