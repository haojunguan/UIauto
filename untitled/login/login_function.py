import time


class Login(object):
    def user_login(self, driver, username, password):
        driver.find_element_by_xpath('//*[@id="userId"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//button[@class="layui-btn   masi-login-input masi-login-btn"]').click()
        print('login_function的driver:', driver)
        time.sleep(1)

    def user_quit(self, driver):
        driver.find_element_by_xpath('')
        pass

