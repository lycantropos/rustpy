from contextlib import suppress
from typing import Tuple

from hypothesis import given

from tests.utils import (Integer,
                         equivalence)
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = first - second

        assert isinstance(result, type(first))


@given(strategies.integers_with_zeros)
def test_diagonal(integer_with_zero: Tuple[Integer, Integer]) -> None:
    integer, zero = integer_with_zero

    assert integer - integer == zero


@given(strategies.integers_pairs)
def test_commutative_case(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        assert equivalence(first - second == second - first, first == second)


@given(strategies.integers_with_zeros)
def test_right_neutral_element(
        integer_with_zero: Tuple[Integer, Integer]
) -> None:
    integer, zero = integer_with_zero

    assert integer - zero == integer
