import logging

import allure
import pytest
import yaml

from pythoncode.calculator import calculator


@pytest.fixture()
def get_calc_object():
    logging.info("开始计算")
    calc = calculator()
    yield calc
    logging.info("结束计算")

@allure.story("加载yaml被测数据文件内容")
@pytest.fixture()
def get_datas_calc():
    with open('./datas/calc.yaml') as f:
        # with open('./testing/datas/calc.yaml') as f:
        tatols = yaml.safe_load(f)
    return tatols