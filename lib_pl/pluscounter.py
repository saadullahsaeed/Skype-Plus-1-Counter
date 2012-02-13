import lib_pl.skype_hook

class pluscounter(lib_pl.skype_hook.skype_hook):
    
    TEXT_TO_FIND = '+1'
    CMD_PLUS_ONE = 'plus_1'
    
    def messageReceived(self):
        self.author = self.message.author_displayname
        self.message_text = self.message.body_xml
        self.convo = self.conversation.displayname
        
        print "checking for +1 in: " + self.message_text
        
        if self.isPlusOne :
            print "Got +1"
            params = {'author': self.author, 'convo': self.convo}
            self.notifyWebHook(params)
            return True
        
    
    def isPlusOne(self):
        return self.message_text.find(self.TEXT_TO_FIND) >= 0
    
    
    def getCmd(self):
        return self.CMD_PLUS_ONE
    