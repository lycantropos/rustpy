from hypothesis import given

from rustpy.primitive import bool_
from tests.utils import (Float,
                         equivalence)
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = float_.is_infinite()

    assert isinstance(result, bool_)


@given(strategies.floats)
def test_alternatives(float_: Float) -> None:
    result = float_.is_infinite()

    assert equivalence(result,
                       bool_(not float_.is_finite() and not float_.is_nan()))
