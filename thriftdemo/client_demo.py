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
from ttypes import *
from config import *                          #自定义
import UserService
import traceback
import unittest
import assertpy
import HTMLTestRunner                         #报表
import logging                                #日志

class client(unittest.TestCase):


	def setUp(self):
		transport = self.transport
		transport.open()

	def teardown(self):
		transport = self.transport
		transport.close()


	def test_demo(self):
		pass