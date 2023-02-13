from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import (Integer,
                         integer_to_zero)
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first + second
    except OverflowError:
        pass
    else:
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


@given(strategies.integers)
def test_neutral_element(integer: Integer) -> None:
    zero = integer_to_zero(type(integer))

    assert integer + zero == integer == zero + integer
