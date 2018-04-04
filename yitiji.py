# -*- coding: utf-8 -*-

import unittest ,time 
from appium import webdriver  
from selenium.webdriver.common.keys import Keys
from appium.webdriver.mobilecommand import MobileCommand
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#1.9.0family


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '14105036c824342a078e'
desired_caps['appPackage'] = 'com.xikang.acornapppublichealth'
desired_caps['appActivity'] = 'com.xikang.acorncommonlib.Activity.ReadCardActivity'
desired_caps['unicodeKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
contexts = driver.contexts

driver.find_element_by_id('com.xikang.acornapppublichealth:id/btn_select_resident').click()
driver.implicitly_wait(5)
print contexts 
# driver.tap([(80,204),(324,237)])
driver.find_element_by_xpath('//android.widget.ListView[@resource-id=\"com.xikang.acornapppublichealth:id/content_view\"]/android.widget.LinearLayout[5]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.RadioButton[@resource-id=\"com.xikang.acornapppublichealth:id/button_m\"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.ListView[@resource-id=\"com.xikang.acornapppublichealth:id/lv_maternal\"]/android.widget.LinearLayout[1]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.xikang.acornapppublichealth:id/tv_after_check_status\"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.xikang.acornapppublichealth:id/btn_back\"]').click()
driver.implicitly_wait(5)
assert '789' in driver.find_element_by_id('com.xikang.acornapppublichealth:id/tv_after42_check_status').text
# driver.find_element_by_xpath('//android.widget.Spinner[@resource-id=\"com.xikang.acornapppublichealth:id/resident_filter_spinner\"]').click()
# driver.implicitly_wait(5)
print contexts
# driver.find_element_by_class_name('android.widget.LinearLayout').click()

# driver.tap([(833,262),(1007,295)])
# #print contexts
# #driver.back()
# time.sleep(3)


# driver.implicitly_wait(5)
# driver.tap([(448,115),(884,165)])

# print contexts
