from typing import Type

import pytest
from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.float_types_with_finite_values)
def test_round_trip(float_type_with_float: Float) -> None:
    float_type, float_ = float_type_with_float

    result = float_type.from_ne_bytes(float_.to_ne_bytes())

    assert result is not float_
    assert result == float_


@given(strategies.float_types)
def test_no_bytes(float_type: Type[Float]) -> None:
    with pytest.raises(TypeError):
        float_type.from_ne_bytes(b'')
