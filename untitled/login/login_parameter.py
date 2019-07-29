from selenium import webdriver

from config import *
# from login.login_function import Login
from login import Login


class LoginTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        print('login_parameter的driver1:', self.driver)

    def open_url(self):
        self.driver.get(URL)
        print('login_parameter的openurl的driver:', self.driver)

    def login_yayd(self):
        username = 'ya-csyd'
        password = '123456'
        print('login_parameter的driver2:', self.driver)
        Login().user_login(self.driver, username, password)

    def login_yayy(self):
        username = 'ya-csyy'
        password = '123456'
        Login().user_login(self.driver, username, password)

    def login_akyd(self):
        username = 'ak-csyd'
        password = '123456'
        Login().user_login(self.driver, username, password)

    def login_akyy(self):
        pass