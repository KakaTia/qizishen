from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common import by


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
            # opt = webdriver.ChromeOptions()
            # opt.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=opt)
            # self.driver.implicitly_wait(10)
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            # cookies = self.driver.get_cookies()
            # with open("data.yaml", 'w', encoding="UTF-8") as f:
            #     yaml.dump(cookies, f)
            # with open("data.yaml", "r", encoding="UTF-8") as s:
            #     yaml_data = yaml.safe_load(s)
            # for cookie in yaml_data:
            #     self.driver.add_cookie(cookie)
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