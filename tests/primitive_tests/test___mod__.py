from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.divisible_integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    dividend, divisor = pair

    try:
        result = dividend % divisor
    except OverflowError:
        pass
    else:
        assert isinstance(result, type(dividend))


@given(strategies.divisible_integers_pairs)
def test_connection_with_truediv(pair: Tuple[Integer, Integer]) -> None:
    dividend, divisor = pair

    try:
        result = dividend % divisor
        quotient_times_divisor = (dividend / divisor) * divisor
    except OverflowError:
        pass
    else:
        assert quotient_times_divisor + result == dividend


@given(strategies.integers_with_zeros)
def test_zero_divisor(integer_with_zero: Tuple[Integer, Integer]) -> None:
    integer, zero = integer_with_zero

    with pytest.raises(ZeroDivisionError):
        integer % zero
