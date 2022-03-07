import unittest


class UserCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类执行之前执行")

    def setUp(self):
        print("测试用例之前执行")

    def test_Adduser(self):
        self.assertAlmostEqual("1", "1")
        print("1")

    def test_Insert(self):
        self.assertAlmostEqual("1", "1")
        print("2")

    def tearDown(self):
        print("测试用例之后执行")

    @classmethod
    def tearDownClass(cls):
        print("类执行之后执行")


if __name__ == '__main__':
    unittest.main()
