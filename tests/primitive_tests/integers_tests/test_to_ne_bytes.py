import sys

from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers)
def test_basic(integer_: Integer) -> None:
    result = integer_.to_ne_bytes()

    assert isinstance(result, bytes)


@given(strategies.integers)
def test_alternatives(integer_: Integer) -> None:
    result = integer_.to_ne_bytes()

    assert (sys.byteorder == 'big' and result == integer_.to_be_bytes()
            or sys.byteorder == 'little' and result == integer_.to_le_bytes())
