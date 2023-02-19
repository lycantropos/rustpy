from typing import Type

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integer_types_with_values)
def test_round_trip(integer_type_with_integer: Integer) -> None:
    integer_type, integer = integer_type_with_integer

    result = integer_type.from_le_bytes(integer.to_le_bytes())

    assert result is not integer
    assert result == integer


@given(strategies.integer_types)
def test_no_bytes(integer_type: Type[Integer]) -> None:
    with pytest.raises(TypeError):
        integer_type.from_le_bytes(b'')
