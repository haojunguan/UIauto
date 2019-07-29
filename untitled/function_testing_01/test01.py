# class Test():
#     def __init__(self):
#         self.name = 'aaa'
#
#
#     def function(self):
#         pass
#
# # test1= Test()
# print(Test().name)
import time

try:
    add = 5
    assert(add == 5, '错误')
    # raise NameError('错误')
except Exception as e:
    print(e)
else:
    print('pass')
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))