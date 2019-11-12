"""
@Time    : 2019/11/7 0007 10:01
@Author  : Linyue
@Email   : l_inyue@163.com
@File    : 抖音爬取.py
@name    ：获取用户id
 logcat | grep cmp=   查看报包名
"""
import os
import time
import requests
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Dyid_spider(object):
    def __init__(self):
        self.dy = {
            "platformName": "Android",
            "plateformVersion": "9",
            "deviceName": "1c5bacda",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "splash.SplashActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dy)

    # def open_dy(self):
    #     self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dy)

    def operating(self):
        time.sleep(5)
        # 如果没有文件创建文件
        if not os.path.exists('./DY'):
            os.mkdir("./DY")
        while True:
            dy_use_id = self.get_id()
            with open('./DY/use_id.txt', "a") as f:
                f.write(dy_use_id + '\n')

    def get_id(self):
        print(1)
        try:
            time.sleep(1)
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/ef_').click()
        except:
            try:
                l = self.get_size()
                x = int(l[0] * 0.5)
                y1 = int(l[1] * 0.75)
                y2 = int(l[1] * 0.25)
                self.driver.swipe(x, y1, x, y2)
                time.sleep(1)
                self.get_id()
            except:
                pass
        time.sleep(0.5)
        print('进入个人信息页面')
        self.driver.tap([(953, 112), (1052, 195)])
        # self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/cle').click()
        time.sleep(0.5)
        try:
            self.driver.find_elements_by_xpath('//android.widget.FrameLayout[@content-desc="分享，按钮"]')[0].click()
        except:
            self.driver.back()
            time.sleep(1)
            self.driver.back()
            l = self.get_size()
            x = int(l[0] * 0.5)
            y1 = int(l[1] * 0.75)
            y2 = int(l[1] * 0.25)
            self.driver.swipe(x, y1, x, y2)
            time.sleep(1)
            self.get_id()


        time.sleep(1)
        try:
            self.driver.find_elements_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView')[
                0].click()
        except:
            self.get_id()
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1.5)

        l = self.get_size()
        x = int(l[0] * 0.5)
        y1 = int(l[1] * 0.85)
        y2 = int(l[1] * 0.15)
        self.driver.swipe(x, y1, x, y2)

        dy_url = self.driver.get_clipboard_text().split('！')[1].strip()
        dy_use_id = self.get_redirect_url(dy_url)
        print(dy_use_id)
        return dy_use_id

    def get_redirect_url(self, url):
        # 重定向前的链接
        url = url
        # 请求头，设置了浏览器代理
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        }
        # 请求网页
        response = requests.get(url, headers=headers)
        use_id = response.url.split('/')[5].split("?")[0]  # 打印重定向后的网址
        # 返回重定向后的网址
        return use_id

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        # x1 = int(x * 0.5)
        # y1 = int(x * 0.75)
        # y2 = int(x * 0.25)
        return (x, y)


if __name__ == '__main__':
    wx = Dyid_spider()
    wx.operating()
