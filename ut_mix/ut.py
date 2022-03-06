import unittest


class TestFirst(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1one(self):
        print(1)
        self.assertAlmostEqual(1, 1)

    def test_2two(self):
        print(2)
        self.assertAlmostEqual(2, 2)


class TestSecond(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_3three(self):
        print(3)
        self.assertAlmostEqual(3, 3)

    def test_4four(self):
        print(4)
        self.assertAlmostEqual(4, 4)


if __name__ == "__main__":
    testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestSecond)
    suite = unittest.TestSuite([testcase2])
    unittest.TextTestRunner().run(suite)
