import time
import unittest
import HTMLTestRunner
class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
        self.assertEqual(2 + 3 + 10,15)
    def test_add2(self):
        self.assertEqual(10 + 150,160)
    def test_add3(self):
        #一处出错，查看测试结果
        self.assertEqual(2 * 5 * 7, 40)
    def tearDown(self):
        pass
# def suite():
#     suiteTest=unittest.TestSuite()
#     suiteTest.addTest(testadd("test_add1"))
#     suiteTest.addTest(testadd("test_add2"))
#     suiteTest.addTest(testadd("test_add3"))
#     return suiteTest
if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add1"))
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = "UI_AutoReport_" + now + ".html"
    with open(f"report/{report_path}", "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f)
        runner.run(suite)