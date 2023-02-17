from contextlib import suppress
from typing import Tuple

from hypothesis import given

from tests.utils import (Integer,
                         equivalence)
from . import strategies


@given(strategies.signed_integers)
def test_basic(integer: Integer) -> None:
    with suppress(OverflowError):
        result = integer.abs()

        assert isinstance(result, type(integer))


@given(strategies.signed_integers)
def test_idempotence(integer: Integer) -> None:
    with suppress(OverflowError):
        result = integer.abs()

        assert result == result.abs()


@given(strategies.signed_integers_with_zeros)
def test_positive_definiteness(integer_with_zero: Integer) -> None:
    integer, zero = integer_with_zero

    with suppress(OverflowError):
        result = integer.abs()

        assert equivalence(result == zero, integer == zero)


@given(strategies.signed_integers)
def test_evenness(integer: Integer) -> None:
    with suppress(OverflowError):
        result = integer.abs()

        assert result == (-integer).abs()


@given(strategies.signed_integers_pairs)
def test_multiplicativity(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = (first * second).abs()

        assert result == first.abs() * second.abs()


@given(strategies.signed_integers_pairs)
def test_triangle_inequality(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = (first + second).abs()

        assert result <= first.abs() + second.abs()


@given(strategies.signed_integers_pairs)
def test___mul___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        assert (first * second).abs() == first.abs() * second.abs()


@given(strategies.divisible_signed_integers_pairs)
def test___truediv___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = (first / second).abs()
        alternative = first.abs() / second.abs()

        assert result == alternative
