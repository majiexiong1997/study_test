import pytest


@pytest.fixture(scope='function',autouse=True)
def start_message():
    print('开始计算')
    yield "yield"
    print('计算结束')