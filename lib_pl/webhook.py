import urllib2,httplib,urllib

class webhook:
    
    url = ''
    
    def __init__(self):
        self.donothing = 1
    
    def getUrl(self):
        return self.url
        
    def setParams(self, params):
        self.params = params
        
    
    def setCmd(self, cmd):
        if self.params :
            self.params['cmd'] = cmd
        else:
            self.params = {'cmd': cmd}
            
        
    def callHook(self):
        print self.loadUrl(self.getUrl(), self.params)
            
            
    def loadUrl(self, url, params):
        data = urllib.urlencode(params)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        return response.read()