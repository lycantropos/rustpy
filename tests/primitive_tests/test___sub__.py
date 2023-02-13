from typing import Tuple

from hypothesis import given

from tests.utils import (Integer,
                         equivalence,
                         integer_to_zero)
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first - second
    except OverflowError:
        pass
    else:
        assert isinstance(result, type(first))


@given(strategies.integers)
def test_diagonal(integer: Integer) -> None:
    assert integer - integer == integer_to_zero(type(integer))


@given(strategies.integers_pairs)
def test_commutative_case(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        first_minus_second = first - second
        second_minus_first = second - first
    except OverflowError:
        pass
    else:
        assert equivalence(first_minus_second == second_minus_first,
                           first == second)


@given(strategies.integers)
def test_right_neutral_element(integer: Integer) -> None:
    zero = integer_to_zero(type(integer))

    assert integer - zero == integer
