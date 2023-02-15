from contextlib import suppress
from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.divisible_integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    dividend, divisor = pair

    with suppress(OverflowError):
        result = dividend % divisor

        assert isinstance(result, type(dividend))


@given(strategies.divisible_integers_pairs)
def test_connection_with_truediv(pair: Tuple[Integer, Integer]) -> None:
    dividend, divisor = pair

    with suppress(OverflowError):
        result = dividend % divisor

        assert (dividend / divisor) * divisor + result == dividend


@given(strategies.integers_with_zeros)
def test_zero_divisor(integer_with_zero: Tuple[Integer, Integer]) -> None:
    integer, zero = integer_with_zero

    with pytest.raises(ZeroDivisionError):
        integer % zero
