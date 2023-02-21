from typing import Tuple

from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first & second

    assert isinstance(result, type(first))


@given(strategies.integers_pairs)
def test_commutativity(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first & second

    assert result == second & first


@given(strategies.integers_triplets)
def test_associativity(triplet: Tuple[Integer, Integer, Integer]) -> None:
    first, second, third = triplet

    result = (first & second) & third

    assert result == first & (second & third)


@given(strategies.integers_with_zeros)
def test_absorbing_element(integer_with_zero: Tuple[Integer, Integer]) -> None:
    integer, zero = integer_with_zero

    assert integer & zero == zero == zero & integer
