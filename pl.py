import urllib2,httplib,urllib
from array import array
from lib_pl.pluscounter import *

counter = pluscounter()
hooks = {counter}

def notifyHooks(message, conversation):
    for hook in hooks:
        hook.setMessage(message)
        hook.setConversation(conversation)
        hook.messageReceived()
