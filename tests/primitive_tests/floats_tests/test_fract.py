from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats)
def test_basic(float_: Float) -> None:
    result = float_.fract()

    assert isinstance(result, type(float_))


@given(strategies.finite_floats)
def test_alternatives(float_: Float) -> None:
    result = float_.fract()

    assert result == float_ - float_.trunc()
