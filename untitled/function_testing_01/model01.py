import time
import unittest

from selenium import webdriver


#定点结算管理-结算退费
class Month_table(unittest.TestCase):

    def test_a(self):
        _chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        url = 'http://192.168.128.234/masi-medicare-settlement-web/web/medicare/settlement/common/homepage/index.html'
        driver = webdriver.Chrome(executable_path=_chrome_path)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="userId"]').send_keys('ya-csyd')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        driver.find_element_by_xpath('//button[@class="layui-btn   masi-login-input masi-login-btn"]').click()
        # driver.implicitly_wait(10)
        js = 'var q=document.documentElement.scrollTop=10000'
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[2]').click()
        driver.execute_script(js)
        time.sleep(1)
        driver.find_elements_by_xpath("//ul[@class='layui-nav-sub-list sidebar-sublist']/li[@class='layui-nav-item']")[0].click()   #点击药店退费
        xf = driver.find_element_by_xpath("//div[@id='20180807142350123221']/iframe[@frameborder='no']")
        driver.switch_to_frame(xf)
        # time.sleep(1)
        # driver.execute_script(js)
        driver.find_element_by_xpath('//div[@class="layui-input-block masi-search-input"]/input[@id="retrievalContent"]').send_keys('4265')   #文本框输入内容
        driver.find_element_by_xpath('//div[@class="btn btn-query masi-left"]/p[@lay-filter="masiSearch"]').click()
        driver.find_element_by_xpath('//div[@class="layui-table-cell laytable-cell-1-0-11"]/a[@class="text-primary masi-clickable"]').click()
        # driver.find_element_by_xpath('//div[@class="layui-table-cell laytable-cell-1-0-11"]/a[text()="撤销"')
        driver.find_element_by_xpath('//div[@class="layui-input-block"]/input[@id="IDNumber"]').send_keys('610402199506157494')     #输入身份证号
        driver.find_element_by_xpath('//div[@class="layui-input-block"]/input[@id="ICNum"]').send_keys('2')     #输入医保号
        driver.find_element_by_xpath('//div[@class="layui-layer-btn layui-layer-btn-c"]/a[@class="layui-layer-btn1"]').click()      #点击确定

suite = unittest.TestSuite()
suite.addTest(Month_table('test_a'))
runner = unittest.TextTestRunner()
runner.run(suite)



