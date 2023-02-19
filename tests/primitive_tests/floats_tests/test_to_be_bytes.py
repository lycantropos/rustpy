import sys

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = float_.to_be_bytes()

    assert isinstance(result, bytes)


@given(strategies.floats)
def test_alternatives(float_: Float) -> None:
    result = float_.to_be_bytes()

    assert result == float_.to_le_bytes()[::-1]
    assert sys.byteorder != 'big' or result == float_.to_ne_bytes()
