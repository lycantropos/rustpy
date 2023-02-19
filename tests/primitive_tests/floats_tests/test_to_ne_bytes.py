import sys

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = float_.to_ne_bytes()

    assert isinstance(result, bytes)


@given(strategies.floats)
def test_alternatives(float_: Float) -> None:
    result = float_.to_ne_bytes()

    assert (sys.byteorder == 'big' and result == float_.to_be_bytes()
            or sys.byteorder == 'little' and result == float_.to_le_bytes())
