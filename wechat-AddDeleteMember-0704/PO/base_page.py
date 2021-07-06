import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy

class BasePage:
    # 1. 程序开始init初始化，给driver_base传参，WebDriver默认值给None，跳转主页后传递回来一个driver，driver就不是None执行else
    def __init__(self, driver_base: WebDriver=None):
        # 如果driver为None，就实例化（初始化）一个driver，否则就用它传过来的driver
        if driver_base is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['noReset'] = 'True'
            desired_caps['dontStopAppOnReset'] = 'True'
            # 跳过操作
            desired_caps['skipDeviceInitialization'] = 'True'
            desired_caps['unicodeKeyBroad'] = 'True'
            desired_caps['resetKeyBroad'] = 'True'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)

        else:
            self.driver=driver_base

    def finds(self, by, locator):
        # 多个元素进行封装
        eles = self.driver.find_elements(by, locator)
        return eles

    def find(self, location, element):
        # 一个元素进行封装
        ele = self.driver.find_element(location, element)
        return ele
    def find_and_click(self, location1, element1):
        # 一个元素进行封装
        ele = self.driver.find_element(location1, element1).click()
        return ele

    def back(self, num=1):
        for i in range(num):
            self.driver.back()


    def swipe_find(self, text, num=3):
        '''
        1、添加查找次数
        2、添加 查找文本 的输入参数
        3、添加隐式等待的动态设置
        :param text:
        :param num:
        :return:
        '''
        # 滑动查找元素
        # 优化 隐式等待，提高查找速度
        self.driver.implicitly_wait(1)

        for i in range(num):
            try:

                element = self.find(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了 {i} 次，未找到")

