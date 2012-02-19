import sys, keypair, pl
from time import sleep

sys.path.append(keypair.distroRoot + '/ipc/python')
sys.path.append(keypair.distroRoot + '/interfaces/skype/python')

try:
	import Skype
except ImportError:
    raise SystemExit('Program requires Skype and skypekit modules')

if len(sys.argv) != 3:
	print('Usage: python plus1.py <skypename> <password>')
	sys.exit()
	
accountName = sys.argv[1]
accountPsw  = sys.argv[2]
loggedIn	= False

#OnMessage Handler
def OnMessage(self, message, changesInboxTimestamp, supersedesHistoryMessage, conversation):
	if message.author != accountName:
		pl.notifyHooks(message, conversation)	


#AccountOnChange Handler
def AccountOnChange (self, property_name):
	global loggedIn
	if property_name == 'status':
		if self.status == 'LOGGED_IN':
			loggedIn = True
			print('Logged in now, lets listen to +1s')


Skype.Skype.OnMessage = OnMessage
Skype.Account.OnPropertyChange = AccountOnChange

try:
	MySkype = Skype.GetSkype(keypair.keyFileName)
	MySkype.Start()
except Exception:
	raise SystemExit('Unable to create skype instance')

print('Logging in with ' + accountName)

account = MySkype.GetAccount(accountName)
account.LoginWithPassword(accountPsw, False, False)

while loggedIn == False:
	sleep(1)

print('Listening to +1s now')
raw_input('')

print('Exiting..')
MySkype.stop()