from typing import (Tuple,
                    Type)

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.floats)
def test_basic(float_: Float) -> None:
    result = float(float_)

    assert isinstance(result, float)


@given(strategies.float_types_with_values)
def test_round_trip(
        float_type_with_value: Tuple[Type[Float], Float]
) -> None:
    float_type, float_ = float_type_with_value

    result = float(float_)

    assert (float_.is_nan() and float_type(result).is_nan()
            or float_type(result) == float_)
