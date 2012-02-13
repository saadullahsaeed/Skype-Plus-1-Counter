import lib_pl.plwebhook 

class skype_hook:
    """Skype Hook Abstract class"""
    def setMessage(self, message):
        self.message = message
        
    def setConversation(self, conversation):
        self.conversation = conversation
        
    def getWebhook(self):
        return lib_pl.plwebhook.plwebhook()
    
    
    def notifyWebHook(self, params):
        webHook = self.getWebhook()
        webHook.setParams(params)
        webHook.setCmd(self.getCmd())
        return webHook.callHook()
    
    def getCmd(self):
        return ''
    