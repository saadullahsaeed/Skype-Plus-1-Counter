from lib_pl.skype_hook import *

class pluscounter(skype_hook):
    
    TEXT_TO_FIND = '+1'
    CMD_PLUS_ONE = 'plus1'
    
    def messageReceived(self):
        self.author = self.message.author_displayname
        self.message_text = self.message.body_xml
        self.convo = self.conversation.displayname
        
        if self.message_text.find(self.TEXT_TO_FIND) >= 0 :
            params = {'author': self.author, 'convo': self.convo, 'cmd': self.CMD_PLUS_ONE}
            self.notifyWebHook(params)
            return True
    

    def getCmd(self):
        return self.CMD_PLUS_ONE
    