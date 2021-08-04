import logging
import os
from typing import List

import pytest


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:

    # items 代表 所有的测试用例的列表
    for item in items:
        # 用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def addlogger():
    if not os.path.exists('.\logs'):
        os.makedirs('.\logs')
    logging.basicConfig(level=logging.INFO,
                        # 日志格式
                        # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        # 打印日志的时间
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        # 日志文件存放的目录（目录必须存在）及日志文件名
                        filename='.\logs/report.text',
                        # 打开日志文件的方式
                        filemode='w'
                        )
    logger = logging.getLogger(__name__)
    return logger
logger = addlogger()