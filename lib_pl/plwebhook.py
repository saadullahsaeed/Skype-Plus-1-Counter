from lib_pl.webhook import *

class plwebhook(webhook):
    API_URL = 'http://d01.peanutlabs.com/skypebot/receive.php'
    
    def getUrl(self):
        return self.API_URL