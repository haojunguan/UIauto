import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#辅助管理-读卡器配置
_chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
url = 'http://192.168.128.234/masi-medicare-settlement-web/web/medicare/settlement/common/homepage/index.html'
driver = webdriver.Chrome(executable_path=_chrome_path)
driver.get(url)
driver.find_element_by_xpath('//*[@id="userId"]').send_keys('ya-csyd')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//button[@class="layui-btn   masi-login-input masi-login-btn"]').click()
js = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//ul[@class="layui-nav-sub-list sidebar-sublist"]/li[@data-id="20180807142350123224"]').click()   #读卡器配置
xf = driver.find_element_by_xpath("//div[@id='20180807142350123224']/iframe[@frameborder='no']")
driver.switch_to_frame(xf)
# driver.find_element_by_xpath('//div[@class="layui-btn-container demoTable"]/button[@class="layui-btn layui-btn-radius btn btn-sm"]').click()    #新增读卡器
# xf2 = driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe[@src='./addcard.html?type=1']")
# driver.switch_to_frame(xf2)
# driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@placeholder="请选择读卡器型号"]').click()   #点击下拉框
# driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="新读卡器"]').click()    #点击新读卡器
# driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@placeholder="请选择读卡器型号"]').click()   #再点击下拉框
# driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="旧读卡器"]').click()    #点击旧读卡器
# driver.find_element_by_xpath('//div[@class="layui-input-block"]/input[@placeholder="请输入读卡器端口"]').send_keys('1')
# driver.find_element_by_xpath('//div[@id="masiPopBtn"]/button[text()="保存"]')
driver.find_element_by_xpath('//div[@class="layui-table-cell laytable-cell-1-0-6"]/a[@title="修改"]').click()
xf3 = driver.find_element_by_xpath('//div[@class="layui-layer-content"]/iframe[@src="./addcard.html?type=2"]')
driver.switch_to_frame(xf3)
driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@placeholder="请选择读卡器型号"]').click()
driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="旧读卡器"]').click()
driver.find_element_by_xpath('//div[@class="layui-select-title"]/input[@placeholder="请选择读卡器型号"]').click()
driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="新读卡器"]').click()
driver.find_element_by_xpath('//div[@class="layui-input-block"]/input[@placeholder="请输入读卡器端口"]').send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath('//div[@class="layui-input-block"]/input[@placeholder="请输入读卡器端口"]').send_keys('2')




