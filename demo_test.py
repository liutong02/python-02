from HTMLTestRunner import HTMLTestRunner
from iter_add import login
import unittest
import sys
class Testlogin(unittest.TestCase):
    #初始化方法
     @classmethod
     def setUpClass(cls) -> None:
         print("开始运行",sys._getframe().f_code.co_name)
     #清除方法
     def tearDown(self) -> None:
        print("开始运行",sys._getframe().f_code.co_name)
     def test_login_success(self):#输入正确的用户名和密码
        print("开始运行", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('cade')
        self.assertEqual(except_value,actual_value)
     def test_user_wrong(self):#输入错误的用户名和密码
        print("开始运行", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('dev', '123456').get('cade')
        self.assertEqual(except_value, actual_value)
if __name__ == '__main__':


    # unittest.main()
    suite_a = unittest.TestSuite()
    suite_a.addTest(Testlogin('test_login_success'))
    suite_a.addTest(Testlogin('test_user_wrong'))
    print(suite_a)

    test_report = './test_report.html'
    with open (test_report,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告',description='测试报告描述')
        runner.run(suite_a)


