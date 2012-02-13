import lib_pl.webhook

class plwebhook(lib_pl.webhook.webhook):
    API_URL = 'http://d01.peanutlabs.com/skypebot/receive.php'
    
    def getUrl(self):
        return self.API_URL