import time
import unittest

from config import *
from login.login_parameter import LoginTest
from login import *

#对账管理-药店报表打印-打印月度汇总表
class Month_table(unittest.TestCase):

    def setUp(self):
        print('test Month_table:')

    def test_a(self):
        """六月月度汇总表"""
        l = LoginTest()
        l.open_url()
        l.login_yayd()
        windows1 = l.driver.current_window_handle
        l.driver.implicitly_wait(1)
        # time.sleep(1)
        l.driver.execute_script(JS)
        time.sleep(1)
        title = l.driver.title
        self.assertEqual(title, '云平台-结算软件')
        l.driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[5]').click()
        time.sleep(1)
        l.driver.find_element_by_xpath('//ul[@class="layui-nav-sub-list sidebar-sublist"]/li[@data-id="20180807142350123222"]').click()
        xf = l.driver.find_element_by_xpath("//div[@id='20180807142350123222']/iframe[@frameborder='no']")
        l.driver.switch_to_frame(xf)
        l.driver.find_element_by_xpath('//div[@class="layui-input-block printing-content-block"]/input[@name="downLoadDate"]').click()  #点击对账日期
        l.driver.find_element_by_xpath('//div[@class="layui-laydate-content"]//li[text()="六月"]').click()
        l.driver.find_element_by_xpath('//div[@class="laydate-footer-btns"]/span[text()="确定"]').click()
        l.driver.find_element_by_xpath('//div[@class="layui-form-item masi-printing-content-content-item masi-printing-footer"]/button[text()="确定"]').click()
        all_handles = l.driver.window_handles
        for handle in all_handles:
            if handle != windows1:
                l.driver.switch_to.window(handle)
                time.sleep(3)
                l.driver.close()
        l.driver.quit()

    def test_b(self):
        """七月月度汇总表"""
        l = LoginTest()
        l.open_url()
        l.login_yayd()
        windows1 = l.driver.current_window_handle
        time.sleep(1)
        l.driver.execute_script(JS)
        time.sleep(1)
        l.driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[5]').click()
        time.sleep(1)
        l.driver.find_element_by_xpath(
            '//ul[@class="layui-nav-sub-list sidebar-sublist"]/li[@data-id="20180807142350123222"]').click()
        xf = l.driver.find_element_by_xpath("//div[@id='20180807142350123222']/iframe[@frameborder='no']")
        l.driver.switch_to_frame(xf)
        l.driver.find_element_by_xpath(
            '//div[@class="layui-input-block printing-content-block"]/input[@name="downLoadDate"]').click()  # 点击对账日期
        l.driver.find_element_by_xpath('//div[@class="layui-laydate-content"]//li[text()="七月"]').click()
        l.driver.find_element_by_xpath('//div[@class="laydate-footer-btns"]/span[text()="确定"]').click()
        l.driver.find_element_by_xpath(
            '//div[@class="layui-form-item masi-printing-content-content-item masi-printing-footer"]/button[text()="确定"]').click()
        time.sleep(5)
        l.driver.get_screenshot_as_file('../picture/' + time.strftime("%Y-%m-%d %H_%M_%S") + '汇总表.jpg')
        all_handles = l.driver.window_handles
        for handle in all_handles:
            if handle != windows1:
                l.driver.switch_to.window(handle)
                time.sleep(3)
                l.driver.close()

    def tearDown(self):
        print('test end>>>>>>>>>>>')

# suite = unittest.TestSuite()
# suite.addTest(Month_table('test_a'))
# suite.addTest(Month_table('test_b'))
# runner = unittest.TextTestRunner()
# runner.run(suite)

