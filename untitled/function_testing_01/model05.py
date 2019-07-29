import time

from config import *
from login.login_parameter import LoginTest

#对账管理-药店报表打印-打印月度对账表
l = LoginTest()
l.open_url()
l.login_yayd()
windows1 = l.driver.current_window_handle
time.sleep(1)
l.driver.execute_script(JS)
time.sleep(1)
l.driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[5]').click()
time.sleep(1)
l.driver.find_element_by_xpath('//ul[@class="layui-nav-sub-list sidebar-sublist"]/li[@data-id="20180807142350123222"]').click()
xf = l.driver.find_element_by_xpath("//div[@id='20180807142350123222']/iframe[@frameborder='no']")
l.driver.switch_to_frame(xf)
l.driver.find_element_by_xpath('//div[@class="layui-input-block printing-content-block"]/input[@name="beginEndDate"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-laydate-header"]/i[@class="layui-icon laydate-icon laydate-prev-m"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-laydate-header"]/i[@class="layui-icon laydate-icon laydate-prev-m"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-laydate-content"]//td[@lay-ymd="2019-5-15"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-laydate-content"]//td[@lay-ymd="2019-6-11"]').click()
l.driver.find_element_by_xpath('//div[@class="laydate-footer-btns"]/span[text()="确定"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@value="定点药店购药"]').click()
l.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[@lay-value="15"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@value="定点药店购药"]').click()
l.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[@lay-value="14"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@value="全部"]').click()
l.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[@lay-value="1"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@value="全部"]').click()
l.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="全部"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-form-item masi-printing-content-content-item"]/button[text()="确定"]').click()
all_handles = l.driver.window_handles
for handle in all_handles:
    if handle != windows1:
        l.driver.switch_to.window(handle)
        time.sleep(3)
        l.driver.close()









