from lib_pl.plwebhook import *

class skype_hook:
    """Skype Hook Abstract class"""
    def setMessage(self, message):
        self.message = message
        
    def setConversation(self, conversation):
        self.conversation = conversation
        
    def getWebhook(self):
        return plwebhook()
    
    
    def notifyWebHook(self, params):
        webHook = self.getWebhook()
        webHook.setParams(params)
        #webHook.setCmd(self.getCmd())
        return webHook.callHook()
    
    def getCmd(self):
        return ''

	def getTarget(self):
		return ''
    