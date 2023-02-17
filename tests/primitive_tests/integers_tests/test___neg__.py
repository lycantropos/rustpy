from contextlib import suppress
from typing import Tuple

from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.signed_integers)
def test_basic(integer: Integer) -> None:
    with suppress(OverflowError):
        result = -integer

        assert isinstance(result, type(integer))


@given(strategies.signed_integers)
def test_involution(integer: Integer) -> None:
    with suppress(OverflowError):
        assert -(-integer) == integer


@given(strategies.signed_integers_pairs)
def test___add___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        assert -(first + second) == (-first) + (-second)


@given(strategies.signed_integers_pairs)
def test___sub___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        assert -(first - second) == (-first) - (-second)


@given(strategies.signed_integers_pairs)
def test___mul___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = -(first * second)

        assert result == (-first) * second == first * (-second)


@given(strategies.divisible_signed_integers_pairs)
def test___truediv___operand(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError):
        result = -(first / second)

        assert result == (-first) / second == first / (-second)
