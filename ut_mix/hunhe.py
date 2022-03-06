import unittest
import ut

if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest((ut.TestFirst("test_1one")))
    # suite.addTest((ut.TestSecond("test_3three")))
    # unittest.TextTestRunner().run(suite)
    testSuite = unittest.TestLoader().discover('.')
    print(testSuite)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
