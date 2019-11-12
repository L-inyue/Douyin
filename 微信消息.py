"""
@Time    : 2019/11/7 0007 10:01
@Author  : Linyue
@Email   : l_inyue@163.com
@File    : 微信消息.py
@name    ：微信发送粘贴板信息
"""
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Dy_weixin():
    def __init__(self):
        self.weixin_cap = {
            "platformName": "Android",
            "plateformVersion": "9",
            "deviceName": "1c5bacda",
            "appPackage": "com.tencent.mm",
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            "noReset": True
        }
        self.weixin_driver = None

    def open_weixin(self):
        self.weixin_driver = webdriver.Remote('http://localhost:4723/wd/hub', self.weixin_cap)

    def get_size(self):
        x = self.weixin_driver.get_window_size()['width']
        y = self.weixin_driver.get_window_size()['height']
        # x1 = int(x * 0.5)
        # y1 = int(x * 0.75)
        # y2 = int(x * 0.25)
        return (x, y)

    def operating(self):
        self.open_weixin()
        try:
            if WebDriverWait(self.weixin_driver, 3).until(
                    lambda x: x.find_element_by_xpath("//android.view.View[@text='老王']")):
                self.weixin_driver.find_element_by_xpath("//android.view.View[@text='老王']").click()
                time.sleep(0.5)
        except:
            pass

        try:
            if WebDriverWait(self.weixin_driver, 3).until(
                    lambda x: x.find_element_by_xpath(
                        "//android.widget.EditText[@resource-id='com.tencent.mm:id/aqe']")):
                print(self.weixin_driver.get_clipboard_text())
                self.weixin_driver.find_element_by_xpath(
                    "//android.widget.EditText[@resource-id='com.tencent.mm:id/aqe']").send_keys(
                    self.weixin_driver.get_clipboard_text())
        except:
            pass

        try:
            if WebDriverWait(self.weixin_driver, 3).until(
                    lambda x: x.find_element_by_xpath(
                        "//android.widget.Button[@resource-id='com.tencent.mm:id/aql']")):
                self.weixin_driver.find_element_by_xpath(
                    "//android.widget.Button[@resource-id='com.tencent.mm:id/aql']").click()
        except:
            pass


if __name__ == '__main__':
    wx = Dy_weixin()
    wx.operating()
