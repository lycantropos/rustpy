import sys

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats)
def test_basic(float_: Float) -> None:
    result = float_.to_le_bytes()

    assert isinstance(result, bytes)


@given(strategies.finite_floats)
def test_alternatives(float_: Float) -> None:
    result = float_.to_le_bytes()

    assert result == float_.to_be_bytes()[::-1]
    assert sys.byteorder != 'little' or result == float_.to_ne_bytes()
