import urllib2,httplib,urllib
from array import array
import lib_pl.pluscounter

counter = lib_pl.pluscounter.pluscounter()
hooks = {counter}

def notifyHooks(message, conversation):
    for hook in hooks:
        hook.setMessage(message)
        hook.setConversation(conversation)
        hook.messageReceived()
"""
def AddPlus(author, convo):
    print "Got a +1"
    url = 'http://d01.peanutlabs.com/skypebot/receive.php'
    #populate params
    params = {}
    params['author'] = author
    params['convo'] = convo
    params['cmd'] = 'plus1'
    WebHook(url, params)
    
    
def WebHook(url, params):
    data = urllib.urlencode(params)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()
"""