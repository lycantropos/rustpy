from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats)
def test_basic(float_: Float) -> None:
    result = float_.floor()

    assert isinstance(result, type(float_))


@given(strategies.finite_floats_with_ones)
def test_value(float_with_one: Float) -> None:
    float_, one = float_with_one

    result = float_.floor()

    assert float_ <= result <= float_ + one
    assert result.fract() == type(float_)(0.0)


@given(strategies.finite_floats_with_ones)
def test_alternatives(float_with_one: Float) -> None:
    float_, one = float_with_one

    result = float_.floor()

    assert result == -(-float_).ceil()
    assert result == float_.div_euclid(one)
