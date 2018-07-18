# coding:utf8

from libNaviCoreTestInterfaceStub import *
from config import *
import time,datetime
import sys,csv
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")
from NaviCoreWrap.NaviCoreSearchInterface import NaviCoreSearchInterface
from NaviProcessLibrary import NaviProcessLibrary
from NaviCoreCommon import NaviCoreCommon
from NaviCoreWrap.NaviCoreRPInterface import NaviCoreRPInterface
from NaviCoreWrap.CUtil import CUtil
from NaviCoreWrap.Result import Result


class ICList():
    InstanceID = 0x01
    MAPAPI_HMI_PAGE_03_02_ROUTE_20 = 0x00030214
    VIEW_NAVI_ROUTE_CONFIRM = 0x007FFFFF
    IClist = []
    IClistdic = []


    def dicvalues(self,name):
            if NaviCoreSearchInterface.JCTlist != []:
                i = name
                # for i in name:
                #     # self.output = self.output[i]
                if self.output.has_key(i):
                    self.output[i] = self.ICnamedic
                    pass
                    #list2
                else:
                    for out22 in self.output.values():
                        if type(out22) is dict :
                            output_in = self.output[list(self.output.keys())[list(self.output.values()).index(out22)]]
                            for out2 in output_in.keys():
                                if out2 == i:
                                    output_in[out2] = self.ICnamedic
                                    pass
                                elif type(output_in[out2]) is dict:
                                    for out3 in output_in[out2].keys():
                                        if out3 == i:
                                            output_in[out2][out3] = self.ICnamedic
                                            pass
                                        elif type(output_in[out2][out3]) is dict:
                                            for out4 in output_in[out2][out3].keys():
                                                if out4 == i:
                                                    output_in[out2][out3][out4] = self.ICnamedic
                                                    pass
                                                elif type(output_in[out2][out3][out4]) is dict:
                                                    for out5 in output_in[out2][out3][out4].keys():
                                                        if out5 == i:
                                                            output_in[out2][out3][out4][out5] = self.ICnamedic
                                                            pass
                                                        elif type(output_in[out2][out3][out4][out5]) is dict:
                                                            for out6 in output_in[out2][out3][out4][out5].keys():
                                                                if out6 == i:
                                                                    output_in[out2][out3][out4][out5][out6] = self.ICnamedic
                                                                    pass
                                                                else:
                                                                    print 'out of range'

