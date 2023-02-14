from typing import Tuple

from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.signed_integers)
def test_basic(integer: Integer) -> None:
    try:
        result = -integer
    except OverflowError:
        pass
    else:
        assert isinstance(result, type(integer))


@given(strategies.signed_integers)
def test_involution(integer: Integer) -> None:
    try:
        result = -integer
    except OverflowError:
        pass
    else:
        assert -result == integer


@given(strategies.signed_integers_pairs)
def test___add___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = -(first + second)
        sum_of_negated = (-first) + (-second)
    except OverflowError:
        pass
    else:
        assert result == sum_of_negated


@given(strategies.signed_integers_pairs)
def test___sub___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = -(first - second)
        difference_of_negated = (-first) - (-second)
    except OverflowError:
        pass
    else:
        assert result == difference_of_negated


@given(strategies.signed_integers_pairs)
def test___mul___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = -(first * second)
    except OverflowError:
        pass
    else:
        assert result == (-first) * second == first * (-second)


@given(strategies.signed_integers_pairs)
def test_truediv_operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = -(first / second)

    assert result == (-first) / second == first / (-second)
