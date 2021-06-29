import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 1. 程序开始init初始化，给driver_base传参，WebDriver默认值给None，跳转主页后传递回来一个driver，driver就不是None执行else
    def __init__(self, driver_base: WebDriver=None):
        # 如果driver为None，就实例化（初始化）一个driver，否则就用它传过来的driver
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            cookies = self.driver.get_cookies()
            with open("data.yaml", 'w', encoding="UTF-8") as f:
                yaml.dump(cookies, f)
            with open("data.yaml", "r", encoding="UTF-8") as s:
                yaml_data = yaml.safe_load(s)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        else:
            self.driver=driver_base


    def find(self, location, element):
        # 一个元素进行封装
        ele = self.driver.find_element(location, element)
        return ele

    def finds(self, by, locator):
        # 多个元素进行封装
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_and_click(self, by, locator):
        # 元素的点击操作进行封装
        ele= self.driver.find_element(by, locator)
        ele.click()

    def wait_for_click(self, locator, timeout=20):
        # 等待操作进行封装,element: WebElement的意思是告诉ide这个变量是什么类型，element后面点’点儿‘的时候可以搜到这个类型的方法
        element: WebElement = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        element.click()
        return element

    def close_driver(self):
        self.driver.close()



