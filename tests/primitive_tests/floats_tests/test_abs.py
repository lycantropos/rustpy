from typing import Tuple

from hypothesis import given

from tests.utils import (Float,
                         equivalence)
from . import strategies


@given(strategies.finite_floats)
def test_basic(float_: Float) -> None:
    result = float_.abs()

    assert isinstance(result, type(float_))


@given(strategies.finite_floats)
def test_idempotence(float_: Float) -> None:
    result = float_.abs()

    assert result == result.abs()


@given(strategies.finite_floats_with_zeros)
def test_positive_definiteness(float_with_zero: Float) -> None:
    float_, zero = float_with_zero

    result = float_.abs()

    assert equivalence(result == zero, float_ == zero)


@given(strategies.finite_floats)
def test_evenness(float_: Float) -> None:
    result = float_.abs()

    assert result == (-float_).abs()


@given(strategies.finite_floats_pairs)
def test_multiplicativity(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = (first * second).abs()

    assert result == first.abs() * second.abs()


@given(strategies.finite_floats_pairs)
def test_triangle_inequality(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = (first + second).abs()

    assert result <= first.abs() + second.abs()


@given(strategies.finite_floats_pairs)
def test___mul___operand(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    assert (first * second).abs() == first.abs() * second.abs()


@given(strategies.finite_floats_pairs)
def test___truediv___operand(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = (first / second).abs()
    alternative = first.abs() / second.abs()

    assert result.is_nan() and alternative.is_nan() or result == alternative
