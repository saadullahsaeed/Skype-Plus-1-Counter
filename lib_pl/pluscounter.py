import re
from lib_pl.skype_hook import *

class pluscounter(skype_hook):
    
    TEXT_TO_FIND = '+1'
    CMD_PLUS_ONE = 'plus1'
    
    def getTargetName(self, msg):
	    try:
		    return re.search(r"(@\w*)", msg).group(0)
	    except AttributeError:
		    return ''
		
    def getHashTags(self, msg):
	   return re.findall(r"#(\w+)", msg)
		
    def messageReceived(self):
        author = self.message.author_displayname
        message_text = self.message.body_xml
        convo = self.conversation.displayname
        
        if message_text.find(self.TEXT_TO_FIND) >= 0 :
			target = self.getTargetName(message_text)
			hashTags = re.findall(r"#(\w+)", message_text)			
			params = {'author': author, 'convo': convo, 'cmd': self.CMD_PLUS_ONE, 'target': target, 'hash_tag': hashTags}
			print str(params)
			self.notifyWebHook(params)
			return True
    
    def getCmd(self):
        return self.CMD_PLUS_ONE