from typing import Type

from hypothesis import given

from tests.utils import (Float,
                         Integer,
                         Numeric)
from . import strategies


@given(strategies.integers, strategies.numeric_types)
def test_basic(integer: Integer, numeric_type: Type[Numeric]) -> None:
    result = integer.as_(numeric_type)

    assert isinstance(result, numeric_type)


@given(strategies.integers, strategies.float_types)
def test_float_type(integer: Integer, float_type: Type[Float]) -> None:
    result = integer.as_(float_type)

    assert not result.is_nan()
    assert result.trunc() == result
