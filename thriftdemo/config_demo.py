# -*- coding: utf-8 -*-

from thrift import Thrift	 
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient 
import sys	
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('./gen-py')  
import ttypes
import UserService 
import assertpy
import unittest
