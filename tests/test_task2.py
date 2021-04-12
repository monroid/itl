import pytest
import re
from hamcrest import assert_that, empty, equal_to


class TestApp:
    @pytest.mark.parametrize('set_in', [
        ["3", "1", "0"],
        ["3", "1", "-1"],
        ["3", "-1", "-1"],
        ["3", "1", "6"],
        ["3", "1", "d"],
    ])
    def test_number_of_dices(self, app, set_in):
        res = app.run(set_in)
        assert_that("Incorrect number of dices" in res.stdout)

    @pytest.mark.parametrize('set_in', [
        ["3", "0"],
        ["3"],
        [],
        ["3", "1", "3", "d"],
        ["3", "1", "2", "4"]
    ])
    def test_number_of_args(self, app, set_in):
        res = app.run(set_in)
        assert_that("Incorrect number of arguments" in res.stdout)

    @pytest.mark.parametrize('set_in', [
        ["-1", "1", "2"],
        ["1005000000000", "2", "3"],
    ])
    def test_number_of_throws(self, app, set_in):
        res = app.run(set_in)
        assert_that("Incorrect number of throws" in res.stdout)

    @pytest.mark.parametrize('set_in', [
        ["0", "1", "1"],
        ["d", "2", "3"]
    ])
    def test_some_tricky(self, app, set_in):
        res = app.run(set_in)
        assert_that(res.stdout, empty())

    @pytest.mark.parametrize('set_in', [
        ["1", "1", "5"],
        ["50", "2", "3"],
        ["1000", "2", "5"],
        ["1000000", "1", "5"],
    ])
    def test_correct_throws(self, app, set_in):
        res = app.run(set_in)
        assert_that(len(res.stdout.split("\n")[:-1]), equal_to(int(set_in[0])))

    @pytest.mark.parametrize('set_in', [
        ["1", "1", "5"],
        ["100", "2", "3"],
        ["10000", "2", "5"],
        ["100000", "1", "5"],
    ])
    def test_equal_exist(self, app, set_in):
        res = app.run(set_in)
        for i in res.stdout.split("\n")[:-1]:
            assert_that("=" in i)

    @pytest.mark.parametrize('set_in', [
        ["1", "1", "5"],
        ["139", "2", "3"],
        ["578", "2", "5"],
        ["500000", "1", "4"],
    ])
    def test_correct_num_of_items(self, app, set_in):
        a = int(set_in[1])
        b = int(set_in[-1])
        res = app.run(set_in)
        for i in res.stdout.split("\n")[:-1]:
            m = re.findall(r'\d+', i)
            assert_that(a <= len(m[:-1]) <= b)

    @pytest.mark.parametrize('set_in', [
        ["1", "1", "5"],
        ["279", "2", "5"],
        ["999", "1", "5"],
        ["20789", "1", "4"],
    ])
    def test_correct_nums(self, app, set_in):
        res = app.run(set_in)
        for i in res.stdout.split("\n")[:-1]:
            m = re.findall(r'\d+', i)
            assert_that(set(m[:-1]).issubset({"1", "2", "3", "4", "5", "6"}))

    @pytest.mark.parametrize('set_in', [
        ["1", "1", "5"],
        ["179", "2", "5"],
        ["799", "1", "5"],
        ["90789", "3", "5"],
    ])
    def test_correct_sums(self, app, set_in):
        res = app.run(set_in)
        for i in res.stdout.split("\n")[:-1]:
            m = re.findall(r'\d+', i)
            one = m[:-1].count("1")
            five = m[:-1].count("5")
            sum = int(m[-1])
            if sum != 150:
                assert_that(one * 10 + 5 * five == sum)
            else:
                assert_that(set(m[:-1]), equal_to({"1", "2", "3", "4", "5"}))
