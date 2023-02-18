from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = float_.neg()

    assert isinstance(result, type(float_))


@given(strategies.floats)
def test_connection_with___neg__(float_: Float) -> None:
    result = float_.neg()

    assert result.is_nan() and float_.is_nan() or result == -float_
