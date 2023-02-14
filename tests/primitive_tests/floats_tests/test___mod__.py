from typing import Tuple

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats_pairs)
def test_basic(pair: Tuple[Float, Float]) -> None:
    dividend, divisor = pair

    result = dividend % divisor

    assert isinstance(result, type(dividend))


@given(strategies.finite_floats_with_zeros)
def test_zero_divisor(float_with_zero: Tuple[Float, Float]) -> None:
    float_, zero = float_with_zero

    result = float_ % zero

    assert result.is_nan()
