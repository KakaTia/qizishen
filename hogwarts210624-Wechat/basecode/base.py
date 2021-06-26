import os
import pytest
from selenium import webdriver



class WindowsDriver():

    @pytest.fixture()
    def getdriver(self):
        self.driver = webdriver.Chrome()

        # browser = os.getenv("browser")
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()
        # elif browser == 'chrome':
        #     self.driver = webdriver.Chrome()
        # else:
        #     self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield self.driver
        # self.driver.quit()
