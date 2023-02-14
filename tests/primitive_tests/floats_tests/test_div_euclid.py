from typing import Tuple

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats_pairs)
def test_basic(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first.div_euclid(second)

    assert isinstance(result, type(first))


@given(strategies.finite_floats_with_zeros)
def test_zero_divisor(float_with_zero: Tuple[Float, Float]) -> None:
    float_, zero = float_with_zero

    result = float_.div_euclid(zero)

    assert result.is_nan() if float_ == zero else result.is_infinite()
