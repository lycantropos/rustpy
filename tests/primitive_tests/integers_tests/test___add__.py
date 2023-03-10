from contextlib import suppress
from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = first + second

        assert isinstance(result, type(first))


@given(strategies.integers_pairs)
def test_commutativity(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first + second
    except OverflowError:
        with pytest.raises(OverflowError):
            second + first
    else:
        assert result == second + first


@given(strategies.integers_triplets)
def test_associativity(triplet: Tuple[Integer, Integer, Integer]) -> None:
    first, second, third = triplet

    with suppress(OverflowError):
        result = (first + second) + third

        assert result == first + (second + third)


@given(strategies.integers_with_zeros)
def test_neutral_element(integer_with_zero: Tuple[Integer, Integer]) -> None:
    integer, zero = integer_with_zero

    assert integer + zero == integer == zero + integer
