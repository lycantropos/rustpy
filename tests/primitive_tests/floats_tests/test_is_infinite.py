from typing import Type

from hypothesis import given

from rustpy.primitive import bool_
from tests.utils import (Float,
                         equivalence)
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = float_.is_infinite()

    assert isinstance(result, bool_)


@given(strategies.float_types)
def test_constants(float_type: Type[Float]) -> None:
    assert float_type.INFINITY.is_infinite()
    assert float_type.NEG_INFINITY.is_infinite()
    assert not float_type.NAN.is_infinite()


@given(strategies.floats)
def test_alternatives(float_: Float) -> None:
    result = float_.is_infinite()

    assert equivalence(result,
                       bool_(not float_.is_finite() and not float_.is_nan()))
