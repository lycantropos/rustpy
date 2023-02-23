from typing import (Tuple,
                    Type,
                    Union)

from hypothesis import given

from tests.utils import (Bool,
                         Integer,
                         equivalence)
from . import strategies


@given(strategies.bools, strategies.convertible_from_bool_types)
def test_basic(bool_: Bool, type_: Type[Union[Bool, Integer]]) -> None:
    result = bool_.as_(type_)

    assert isinstance(result, type_)


@given(strategies.bools, strategies.integer_types_with_zeros_and_ones)
def test_integer_type(
        bool_: Bool,
        integer_type_with_zero_and_one: Tuple[Type[Integer], Integer, Integer]
) -> None:
    integer_type, integer_zero, integer_one = integer_type_with_zero_and_one

    result = bool_.as_(integer_type)

    assert equivalence(bool(result == integer_zero), not bool_)
    assert equivalence(result == integer_one, bool_)


@given(strategies.bool_types_with_values)
def test_bool_type(bool_type_with_value: Tuple[Type[Bool], Bool]) -> None:
    bool_type, bool_ = bool_type_with_value

    result = bool_.as_(bool_type)

    assert equivalence(result, bool_)
