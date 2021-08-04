import pytest
from pytest_encode import logger

@pytest.mark.parametrize("name",["哈利"])
def test_log(name):
    logger.info(f"name:{name}")
