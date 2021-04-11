import pytest
from task1.task1 import Converter
from task2.task2 import App


@pytest.fixture(scope='session')
def converter():
    return Converter()


@pytest.fixture(scope='session')
def app():
    return App("ping")
