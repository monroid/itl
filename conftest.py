import pytest
from task1.task1 import Converter


@pytest.fixture(scope='session')
def converter():
    return Converter()
