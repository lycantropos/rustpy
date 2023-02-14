from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats)
def test_basic(float_: Float) -> None:
    result = float_.trunc()

    assert isinstance(result, type(float_))


@given(strategies.finite_floats_with_ones)
def test_value(float_with_one: Float) -> None:
    float_, one = float_with_one

    result = float_.trunc()

    assert (result - float_).abs() < one


@given(strategies.finite_floats)
def test_alternatives(float_: Float) -> None:
    result = float_.trunc()

    assert result == float_ - float_.fract()
