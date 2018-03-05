# -*- coding: utf-8 -*-

from thrift import Thrift   
#from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient 
import time
import sys   
sys.path.append('D:/thrift/gen-py')  
from ttypes import *
import UserService
import traceback
import logging
import assertpy
sys.path.append('D:/thrift')
from config import *
from client_api import *


transport = THttpClient.THttpClient('10.32.173.200', 8085, '/XK_Phr_Proxy/UserServlet')  # ip  port projectname
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = UserService.Client(protocol)

msg = MessageInfo()
time1 = int(time.time())
msgtime = str(time1)
print msg
msg = {
	'fromPerson' : 'M5A1CFEDBE4B09F03008C774D',
	'toPerson' : 'M55FA54FBE4B0BB9D487A7D17',
	'messageTime' : msgtime,
	'messageType' : '1',
	'messageContent' : '123sgfdg',
	'serviceid' : '',
	'deviceid' : '',
}


try:
	print msg
	assert client.messageNotify(msg) is None
except BaseException , ex :
	print ex
	e = str(ex)
	try:
		assertpy.assert_that(e).contains('HealthServiceException')
	except:
		try:
			assertpy.assert_that(e).contains('HTTP')
		except:
			print ex
			raise TypeError('ICE Error')
		else:
			print ex.message
			raise TypeError('HTTP ERROR')
	else:
		print(e)


'''transport.open()  
#log = open(time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt",'wb')
a = ttypes.AccountInfo()
a.userId = 'M5A1CFEDBE4B09F03008C774D'
a.accountName = '15040344536'
a.password = '123456'
a.deviceId = 'awifidc:44:27:96:e9:ea'
mif = ttypes.MemberInfo()
print 'start'
a = client.findXKAccountByProofNum(conf.lonidentify).userId
print a

print 'end'
transport.close()'''
