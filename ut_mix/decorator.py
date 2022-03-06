import unittest


class TestFirst(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    @unittest.skip('跳过当前方法')
    def test_1one(self):
        print(1)
        self.assertAlmostEqual(1, 1)

    def test_2two(self):
        print(2)
        self.assertAlmostEqual(2, 2)


class TestSecond(unittest.TestCase):
    a=4
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_3three(self):
        print(3)
        self.assertAlmostEqual(3, 3)
    @unittest.skipIf(a>3,'info')
    def test_4four(self):
        print(4)
        self.assertAlmostEqual(4, 4)

    @unittest.skipIf(a == 3, 'info')
    def test_5four(self):
        print(5)
        self.assertAlmostEqual(5, 5)

if __name__ == "__main__":
    # unittest.main()

    testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestSecond)
    suite = unittest.TestSuite([testcase2])
    unittest.TextTestRunner().run(suite)
