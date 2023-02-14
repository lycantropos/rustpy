from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats_pairs)
def test_basic(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first.rem_euclid(second)

    assert isinstance(result, type(first))


@given(strategies.finite_floats_with_zeros)
def test_zero_divisor(float_with_zero: Tuple[Float, Float]) -> None:
    float_, zero = float_with_zero

    result = float_.rem_euclid(zero)

    assert result.is_nan()
