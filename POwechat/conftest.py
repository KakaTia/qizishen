from typing import List
import yaml
from selenium import webdriver

# 改写 pytest_collection_modifyitems hook 函数，
# 收集上来所有的测试用例之后，修改items的方法
# 一般hook 会放在conftest.py 文件中，
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        # item.name 测试用例的名字
        # item.nodeid 测试用例的路径
        # print(item.name)
        # print(item.nodeid)
        # 修改测试用例的编码
        item.name = item.name.encode('UTF-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('UTF-8').decode('unicode-escape')

def test_load_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
    driver.quit()
