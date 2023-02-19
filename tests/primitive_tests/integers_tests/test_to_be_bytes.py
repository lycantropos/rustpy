import sys

from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers)
def test_basic(integer_: Integer) -> None:
    result = integer_.to_be_bytes()

    assert isinstance(result, bytes)


@given(strategies.integers)
def test_alternatives(integer_: Integer) -> None:
    result = integer_.to_be_bytes()

    assert result == integer_.to_le_bytes()[::-1]
    assert sys.byteorder != 'big' or result == integer_.to_ne_bytes()
