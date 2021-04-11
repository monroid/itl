import pytest
from task1.task1 import ValueCannotBeConvertedError


class TestConverter:
    @pytest.mark.xfail(raises=ValueCannotBeConvertedError)
    @pytest.mark.parametrize('test_in', [
        ("30", 30),
        ("30s", 30),
        ("S", 1),
        ("60.5m", 3630),
        ("10seconds", None),
        ("1m30s", None),
        ("1y", None),
        ("", None)]
    )
    def test_converter_work(self, test_in, converter):
        res = converter.to_seconds(test_in[0])
        print(res)
        assert res == test_in[1]

