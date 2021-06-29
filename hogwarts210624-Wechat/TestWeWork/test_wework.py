import os
import time
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure
import yaml
import logging

from TestWeWork.conftest import get_memberinfo


@allure.feature("登录获取cookie")
class TestLogin():
    @allure.story("复用操作-打开chrome")
    @allure.title("复用操作-登录企业微信获取cookie")
    @pytest.mark.skip
    def test_login(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        # print(getdriver.get_cookies())
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element_by_id("menu_contacts").click()
        sleep(3)
        cookies = driver.get_cookies()
        with open("TestWeWork/data.yaml", 'w', encoding="UTF-8") as f:
            yaml.dump(cookies, f)


# @pytest.mark.skip
@allure.feature("添加成员模块")
class Testwework():
    @allure.story("使用cookie跳过登录扫码")
    @allure.title("打开浏览器传cookie")
    @pytest.fixture(scope="class")
    def testing(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # with open("data.yaml", encoding="UTF-8") as f:
        # 在data.yaml文件里已有的cookie，添加到浏览器，
        with open("TestWeWork/data.yaml", "r", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 隐式等待
        driver.implicitly_wait(10)
        # 返回driver
        yield driver
        # 关闭浏览器
        driver.quit()

    # @pytest.mark.skip

    # 参数化获取yaml文件里面的成员信息
    @pytest.mark.parametrize('name,englishname,acctid,phone,mail,expect', get_memberinfo()['info'],
                             ids=get_memberinfo()['ids'])
    @allure.story("企业微信添加成员")
    @allure.title("通讯录添加成员")
    # 将成员信息和driver传入添加成员这个方法中，进行使用
    def test_wework_addmember(self, name, englishname, acctid, phone, mail, expect, testing):
        driver = testing
        driver.implicitly_wait(8)
        driver.find_element_by_id("menu_contacts").click()
        time.sleep(2)
        # 点击添加成员
        with allure.step("点击添加成员"):
            driver.find_element(By.XPATH, '//*[@class="js_has_member"]/div[1]/a[1]').click()
            # 等待
         # 手机和邮箱不能同时为空，请更改信息，截图保存在allure报告中


            if name == 'nameempyt':
                driver.find_element(By.ID, 'memberAdd_acctid').send_keys(acctid)
                with allure.step(f"{name}的为空，截图保存在allure报告中"):
                    logging.info(f"{name}的为空，截图保存在allure报告中")
                    driver.find_element(By.LINK_TEXT, '保存').click()

                    # driver.find_elements_by_xpath("//*[contains(text(), '手机和邮箱不能同时为空')]")
                    time.sleep(1)
                    driver.save_screenshot(f"./TestWeWork/screenshots/请检查用户-{acctid}的name为空.png")
                    allure.attach.file(fr'./TestWeWork/screenshots/请检查用户-{acctid}的name为空.png',
                                       attachment_type=allure.attachment_type.PNG)
                    driver.find_element(By.LINK_TEXT, '取消').click()
                    assert expect == 'nameempyt'

            elif name == 'phonenameempyt':
                with allure.step(f"{name}的手机和邮箱不能同时为空，截图保存在allure报告中"):
                    driver.find_element(By.ID, 'username').send_keys(name)
                    driver.find_element(By.ID, 'memberAdd_english_name').send_keys(englishname)
                    driver.find_element(By.ID, 'memberAdd_acctid').send_keys(acctid)

                    logging.info(f"{name}的手机和邮箱不能同时为空，截图保存在allure报告中")
                    driver.find_element(By.LINK_TEXT, '保存').click()

                    # driver.find_elements_by_xpath("//*[contains(text(), '手机和邮箱不能同时为空')]")
                    time.sleep(1)
                    driver.save_screenshot(f"./TestWeWork/screenshots/请检查用户-{name}手机和邮箱不能同时为空.png")
                    allure.attach.file(fr'./TestWeWork/screenshots/请检查用户-{name}手机和邮箱不能同时为空.png',
                                       attachment_type=allure.attachment_type.PNG)
                    driver.find_element(By.LINK_TEXT, '取消').click()
                    assert expect == 'phonenameempyt'
                    time.sleep(1)
            else:

                logging.info(f"添加成员{name}信息")
                driver.find_element(By.ID, 'username').send_keys(name)
                driver.find_element(By.ID, 'memberAdd_english_name').send_keys(englishname)
                driver.find_element(By.ID, 'memberAdd_acctid').send_keys(acctid)
                driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
                driver.find_element(By.ID, 'memberAdd_mail').send_keys(mail)

                # 保存成员信息
                driver.find_element(By.LINK_TEXT, '保存').click()

                if driver.find_elements_by_xpath("//*[contains(text(), '请填写正确的邮箱地址')]"):
                    with allure.step(f"{name}的成员邮箱地址不正确{mail}，截图保存在allure报告中"):
                        logging.info(f"{name}的成员邮箱地址不正确{mail}，截图保存在allure报告中")
                        driver.save_screenshot(f"./TestWeWork/screenshots/请检查用户-{name}邮箱{mail}不正确.png")
                        allure.attach.file(fr'./TestWeWork/screenshots/请检查用户-{name}邮箱{mail}不正确.png',
                                           attachment_type=allure.attachment_type.PNG)
                        driver.find_element(By.LINK_TEXT, '取消').click()
                        assert expect =="mailFAIL"
                        time.sleep(1)

                elif driver.find_elements_by_xpath("//*[contains(text(), '该帐号已被')]") and driver.find_elements_by_xpath("//*[contains(text(), '占有')]"):
                    with allure.step(f"{name}的成员账号{acctid}信息已被占有，截图保存在allure报告中"):
                        # {name}的成员账号{acctid}信息已经存在，放日志中

                        logging.info(f"{name}的成员账号{acctid}信息已被占有，截图保存在allure报告中")
                        driver.save_screenshot(f"./TestWeWork/screenshots/请检查用户-{name}账号{acctid}已被占有.png")
                        allure.attach.file(fr'./TestWeWork/screenshots/请检查用户-{name}账号{acctid}已被占有.png',
                                           attachment_type=allure.attachment_type.PNG)
                        driver.find_element(By.LINK_TEXT, '取消').click()
                        assert expect =="acctidexsit"
                        time.sleep(1)

                elif driver.find_elements_by_xpath("//*[contains(text(), '该邮箱已被')]"):
                    with allure.step(f"{name}邮箱{mail}已被占有，截图保存在allure报告中"):
                        logging.info(f"{name}的成员邮箱{mail}已被占有，截图保存在allure报告中")
                        driver.save_screenshot(f"./TestWeWork/screenshots/请检查用户-{name}邮箱{mail}已被占有.png")
                        allure.attach.file(fr'./TestWeWork/screenshots/请检查用户-{name}邮箱{mail}已被占有.png',
                                           attachment_type=allure.attachment_type.PNG)
                        driver.find_element(By.LINK_TEXT, '取消').click()
                        assert expect =="mailexsit"
                        time.sleep(1)

