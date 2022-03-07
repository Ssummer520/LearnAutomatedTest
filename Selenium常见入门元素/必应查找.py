import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def getcookie():
    cookies = driver.get_cookies()
    if len(cookies)==0:
        print("没有cookie数据了")
    for c in cookies:
        print(c)


while 1:

    driver.get("https://cn.bing.com/?mkt=zh-CN")
    element = driver.find_element(By.ID, 'sb_form_q')
    element.send_keys('俄罗斯')
    element = driver.find_element(By.ID, 'sb_form_go')
    element.submit()


    element = driver.find_element(By.LINK_TEXT, '俄罗斯（俄罗斯联邦）_百度百科 - Baidu')
    element.click()
    print(driver.title)
    print(driver.current_url)
    print(element)
    # getcookie()
    print(1234)
    # print(driver.get_cookie('MUIDB'))
    # driver.delete_cookie("MUIDB")
    # getcookie()
    # driver.delete_all_cookies()
    # getcookie()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.forward()
    driver.get("https://www.runoob.com/")
    driver.refresh()
    time.sleep(1)

driver.close()



