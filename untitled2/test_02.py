# test_02.py文件

from selenium import webdriver
import time

# ** 作者：上海-悠悠 QQ交流群：646645429**

def test_yoyo_01(browser = webdriver.Chrome()):

    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert "上海-悠悠" in t