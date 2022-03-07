import unittest

first = 50


class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        # print(first+50)
        pass

    def test_Sum(self):
        second = first + 100
        self.assertAlmostEqual(second, 150)
        print(second)

    def test_Del(self):
        third = first - 1
        self.assertAlmostEqual(49, 49)
        print(third)

    def tearDown(self) -> None:
        # print(first+50)
        pass


if __name__ == "__main__":
    unittest.main()
