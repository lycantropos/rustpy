from typing import (Tuple,
                    Type)

from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers)
def test_basic(integer: Integer) -> None:
    result = int(integer)

    assert isinstance(result, int)


@given(strategies.integer_types_with_values)
def test_round_trip(
        integer_type_with_value: Tuple[Type[Integer], Integer]
) -> None:
    integer_type, integer = integer_type_with_value

    result = int(integer)

    assert integer_type(result) == integer
