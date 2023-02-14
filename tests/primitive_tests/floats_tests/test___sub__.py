from typing import Tuple

from hypothesis import given

from tests.utils import (Float,
                         equivalence)
from . import strategies


@given(strategies.finite_floats_pairs)
def test_basic(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first - second

    assert isinstance(result, type(first))


@given(strategies.finite_floats_with_zeros)
def test_diagonal(float_with_zero: Tuple[Float, Float]) -> None:
    float_, zero = float_with_zero

    assert float_ - float_ == zero


@given(strategies.finite_floats_pairs)
def test_commutative_case(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    assert equivalence(first - second == second - first, first == second)


@given(strategies.finite_floats_with_zeros)
def test_right_neutral_element(
        float_with_zero: Tuple[Float, Float]
) -> None:
    float_, zero = float_with_zero

    assert float_ - zero == float_
