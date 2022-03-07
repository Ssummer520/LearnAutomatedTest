import HTMLTestRunner
import unittest
from io import StringIO
if __name__ == "__main__":
    testSuite = unittest.TestLoader().discover('.')
    # unittest.TextTestRunner(verbosity=2).run(testSuite)
    filename="C:\\Users\不为谁而作歌\Desktop\测试报告.html"
    with open(filename,"wb") as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="这里是报告的标题",description="这里是报告的信息")
        runner.run(testSuite)