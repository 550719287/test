# -*- coding: utf-8 -*-

from thrift import Thrift	
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient      #开发使用的thrift框架http请求，需要进入python在thrift包里找到合适的对应方法
import time
import sys	
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('./gen-py')  
# from ttypes import *
# from config import *                          #自定义
import UserService
import traceback
import unittest
import assertpy
import HTMLTestRunner                         #报表
import logging                                #日志

class client(unittest.TestCase):

	def __init__(self):


	#接口地址配置
		ipaddr = '10.32.173.200'
		#服务器地址
		port = 8085
		#端口号
		projectname = '/XK_Phr_Proxy/UserServlet'

		transport = THttpClient.THttpClient(ipaddr ,port ,projectname)  # ip  port projectname
		self.transport = TTransport.TBufferedTransport(transport)
		protocol = TBinaryProtocol.TBinaryProtocol(transport)
		self.client = UserService.Client(protocol)


	def setUp(self):
		transport = self.transport
		transport.open()

	def teardown(self):
		transport = self.transport
		transport.close()


	def test_demo(self):
		pass


if __name__ == "__main__":

	suite = unittest.TestSuite(client().test_demo) 
	# fr = open(localaddr_branch,'wb')
	# runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
	runner.run(suite)