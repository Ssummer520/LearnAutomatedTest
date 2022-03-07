import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginModule(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get_cookies()
        self.driver.get("https://account.cnblogs.com/signin")

    def test_LoginFailed(self):
        time.sleep(1)
        inputName = self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
        inputName.clear()
        inputName.send_keys("33333")
        password = self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
        password.send_keys("33333")
        self.driver.find_element(By.XPATH,
                                 '/html/body/app-root/app-sign-in-layout/div/div/app-sign-in/app-content-container/div/div/div/form/div/button').click()

        try:
            ret = self.driver.find_element(By.XPATH,
                                           '/html/body/app-root/app-sign-in-layout/div/div/app-sign-in/app-content-container/div/div/div/div/div[1]')
            self.assertAlmostEqual(1, 1)
        except:
            raise

    def test_LoginSuccess(self):
        time.sleep(1)
        inputName = self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
        inputName.clear()
        inputName.send_keys("33333")
        password = self.driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
        password.send_keys("33333")
        self.driver.find_element(By.XPATH,
                                 '/html/body/app-root/app-sign-in-layout/div/div/app-sign-in/app-content-container/div/div/div/form/div/button').click()
        title = self.driver.title
        self.assertAlmostEqual(title, '博客园')
        time.sleep(10)

    def tearDown(self) -> None:
        print('测试完成了')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
