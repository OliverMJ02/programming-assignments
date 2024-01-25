# solution cell
# the line below brings the function `convert_days_to_ymd` into scope

from convert_days_to_ymd_solution import convert_days_to_ymd
from nose.tools import assert_equal

### BEGIN SOLUTION


def test_convert_days_to_ymd() -> None:
    assert_equal(convert_days_to_ymd(30.4375 * 10 + 0.5), [0, 10, 0])
    assert_equal(convert_days_to_ymd(30.4375 * 10 + 1.5), [0, 10, 1])
    assert_equal(convert_days_to_ymd(365.25 * 7 + 30.4375 * 10 + 7.9), [7, 10, 7])
    print("OK")


### END SOLUTION
