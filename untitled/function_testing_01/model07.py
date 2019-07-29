import os
import time
import selenium.webdriver.support.ui as ui


start = time.clock()
print(start)
path1 = os.path.abspath(__file__)
print(path1)
path3 = os.path.split(os.path.realpath(__file__))[0]
print(path3)
path2 = os.getcwd()
print(path2)
print(os.path.abspath('function'))
print(os.path.join(path1,'testrunner'))
end = time.clock()







