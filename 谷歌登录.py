import base64
import re
import time

import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def base64img2file(imgsrc: str):
    suffix = imgsrc.split(';')[0][11:]
    with open("demo." + suffix, 'wb') as f:
        f.write(base64.b64decode(imgsrc.split(',')[1]))
def  getcode():
    ocr = ddddocr.DdddOcr()
    time.sleep(1)
    js = '''let c = document.createElement('canvas');let ctx = c.getContext('2d');
let img = document.getElementById("captchaimg"); console.log(img)
c.height=img.naturalHeight;c.width=img.naturalWidth;
ctx.drawImage(img, 0, 0,img.naturalWidth, img.naturalHeight)
let base64String = c.toDataURL();return  base64String'''
    base64_str = driver.execute_script(js)
    # data = base64_str.replace('data:image/png;base64,', '')
    base64_str=re.sub('data:image/png;base64,','',base64_str)
    print(base64_str)
    res = ocr.classification(None,base64_str)
    print(res)
    driver.find_element(By.ID,'ca').send_keys(res)
def getcookie():
    cookies = driver.get_cookies()
    if len(cookies)==0:
        print("没有cookie数据了")
    for c in cookies:
        print(c)
def main():

    driver.get("https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync")
    driver.refresh()
    driver1 = driver.find_element(By.ID, 'identifierId')
    driver1.send_keys("#########")
    divs= driver.find_element(By.ID,'identifierNext')
    divs.click()
    print('我点击了')
    getcode()
    time.sleep(8)
    divs.click()
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('#########')
    divs= driver.find_element(By.ID,'passwordNext')
    divs.click()

if __name__ == '__main__':
    main()



