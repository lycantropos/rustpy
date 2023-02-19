from typing import (Tuple,
                    Type)

from hypothesis import given

from tests.utils import (Float,
                         Integer,
                         Numeric,
                         equivalence,
                         implication)
from . import strategies


@given(strategies.floats, strategies.numeric_types)
def test_basic(float_: Float, numeric_type: Type[Numeric]) -> None:
    result = float_.as_(numeric_type)

    assert isinstance(result, numeric_type)


@given(strategies.floats_with_zeros, strategies.integer_types_with_zeros)
def test_integer_type(
        float_with_zero: Tuple[Float, Float],
        integer_type_with_zero: Tuple[Type[Integer], Integer]
) -> None:
    float_, float_zero = float_with_zero
    integer_type, integer_zero = integer_type_with_zero

    result = float_.as_(integer_type)

    assert equivalence(float_.is_nan() or (float_.trunc() <= float_zero
                                           if integer_type.MIN == integer_zero
                                           else float_.trunc() == float_zero),
                       result == integer_zero)
    assert implication(float_.is_infinite(), result == (integer_type.MAX
                                                        if float_ > float_zero
                                                        else integer_type.MIN))
