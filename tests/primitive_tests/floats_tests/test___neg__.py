from typing import Tuple

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = -float_

    assert isinstance(result, type(float_))


@given(strategies.floats)
def test_involution(float_: Float) -> None:
    assert -(-float_) == float_ or float_.is_nan()


@given(strategies.finite_floats_pairs)
def test___add___operand(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    assert -(first + second) == (-first) + (-second)


@given(strategies.finite_floats_pairs)
def test___sub___operand(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    assert -(first - second) == (-first) - (-second)


@given(strategies.finite_floats_pairs)
def test___mul___operand(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = -(first * second)

    assert result == (-first) * second == first * (-second)


@given(strategies.finite_floats_pairs)
def test___truediv___operand(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = -(first / second)

    assert result.is_nan() or result == (-first) / second == first / (-second)
