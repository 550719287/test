# -*- coding: UTF-8 -*- 
import urllib
import urllib2
import xmltodict


url = 'http://10.32.151.35:9091/cityapi/rest/sensordi/yuwell'

data = {
"param" : "<xml> <device_sn>95FF13AFB4E803F2</device_sn> <device_user>0000</device_user> <device_type>000</device_type> <device_battery>98</device_battery> <mnc>0</mnc> <lac>52c0</lac> <cid>7031</cid> <measure_data>     <sbp>120</sbp>  <dbp>80</dbp>   <pulse_rate>60</pulse_rate>     <arrhythmia>0</arrhythmia>     <measure_time>2014-09-09 10:10:00</measure_time> </measure_data> </xml> ",
"device_sn" : "95FF13AFB4E803F2",
"device_user" : "0000",
"device_type" : "000",
"device_battery" : "98",
"mnc" : "0",
"lac" : "52c0",
"cid" : "7031",
"measure_data" : {
	"sbp" : "120",
	"dbp" : "80",
	"pulse_rate" : "60",
	"arrhythmia" : "0",
	"measure_time" : "2014-09-09 10:10:00"
	}


}

set_data = urllib.urlencode(data)
post = urllib2.Request(url=url,data=set_data,headers={'Content-Type':'application/xml'})  #设置headers传参格式
response = urllib2.urlopen(post)
result = response.read()

print result  #获取到接口信息