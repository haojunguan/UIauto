import time

from login.login_parameter import LoginTest


#统计查询-药店结算查询-结算汇总打印
l = LoginTest()
l.open_url()
l.login_yayd()
print('model03的driver:', l.driver)
print(l)

windows1 = l.driver.current_window_handle
time.sleep(2)
js = 'var q=document.documentElement.scrollTop=10000'
l.driver.execute_script(js)
time.sleep(2)
l.driver.find_element_by_xpath('//*[@id="sidebar"]/ul[1]/li[4]').click()
time.sleep(2)
l.driver.find_element_by_xpath('//ul[@class="layui-nav-sub-list sidebar-sublist"]/li[@data-id="20180807142350123230"]').click()
xf = l.driver.find_element_by_xpath("//div[@id='20180807142350123230']/iframe[@frameborder='no']")
l.driver.switch_to_frame(xf)
l.driver.find_element_by_xpath('//div[@class="layui-btn-container"]/button[@lay-event="printStatement"]').click()    #结算汇总打印
xf2 = l.driver.find_element_by_xpath("//div[@class='layui-layer-content']/iframe[@src='./printstatement.html']")
l.driver.switch_to_frame(xf2)
l.driver.find_elements_by_xpath('//div[@class="layui-select-title"]/input[@placeholder="全部"]')[0].click()     #点击就医类别下拉框
l.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="定点药店购药"]').click()     #点击定点药店购药
l.driver.find_element_by_xpath('//div[@class="layui-input-block"]/input[@placeholder="请选择时间"]').click()   #
l.driver.find_elements_by_xpath('//div[@class="layui-laydate-header"]/i[@class="layui-icon laydate-icon laydate-prev-m"]')[0].click()
l.driver.find_element_by_xpath('//div[@class="layui-laydate-content"]//td[@lay-ymd="2019-6-20"]').click()
l.driver.find_element_by_xpath('//div[@class="layui-laydate-content"]//td[@lay-ymd="2019-7-24"]').click()
l.driver.find_element_by_xpath('//div[@class="laydate-footer-btns"]/span[text()="确定"]').click()
l.driver.find_elements_by_xpath('//div[@class="layui-select-title"]/input[@placeholder="全部"]')[1].click()     #点击统筹区
l.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[text()="延安市市本级"]').click()     #点击延安市
l.driver.find_element_by_xpath('//div[@class="layui-form-item"]/button[text()="确定"]').click()
all_handles = l.driver.window_handles
for handle in all_handles:
    if handle != windows1:
        l.driver.switch_to.window(handle)
        time.sleep(3)
        l.driver.close()




# for handle2 in all_handles:
#     if handle2 == windows1:
#         driver.switch_to.window(handle2)
#         xf3 = driver.find_element_by_xpath("//div[@class='layui-tab-item']/iframe[@src='../../statistical-query/settlementresultquery/settlementresultquery.html?1563877540']")
#         driver.switch_to_frame(xf3)
#         # driver.find_element_by_xpath('//span[@class="layui-layer-setwin"]/a[@class="layui-layer-ico layui-layer-close layui-layer-close1"]').click()
#         driver.find_element_by_xpath('//div[@class="layui-form-item"]/button[text()="确定"]')




