from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats)
def test_basic(float_: Float) -> None:
    result = float_.round()

    assert isinstance(result, type(float_))


@given(strategies.finite_floats_with_ones)
def test_value(float_with_one: Float) -> None:
    float_, one = float_with_one
    integer_part, fractional_part = float_.trunc(), float_.fract()

    result = float_.round()

    assert (result
            == (integer_part
                + ((one if fractional_part >= type(float_)(0.0) else -one)
                   if type(float_)(2.0) * fractional_part.abs() >= one
                   else type(float_)(0.0))))
