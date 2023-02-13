from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first.rem_euclid(second)
    except (OverflowError, ZeroDivisionError):
        pass
    else:
        assert isinstance(result, type(first))


@given(strategies.divisible_integers_pairs)
def test_connection_with_rem_euclid(pair: Tuple[Integer, Integer]) -> None:
    dividend, divisor = pair

    try:
        result = dividend.rem_euclid(divisor)
        euclid_quotient_times_divisor = dividend.div_euclid(divisor) * divisor
    except OverflowError:
        pass
    else:
        assert euclid_quotient_times_divisor + result == dividend


@given(strategies.integers_with_zeros)
def test_zero_divisor(integer_with_zero: Tuple[Integer, Integer]) -> None:
    integer, zero = integer_with_zero

    with pytest.raises(ZeroDivisionError):
        integer.rem_euclid(zero)
