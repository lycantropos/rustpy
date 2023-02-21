from contextlib import suppress
from typing import Tuple

from hypothesis import given

from rustpy.primitive import bool_
from tests.utils import (Integer,
                         equivalence)
from . import strategies


@given(strategies.signed_integers)
def test_basic(integer: Integer) -> None:
    result = integer.is_positive()

    assert isinstance(result, bool_)


@given(strategies.signed_integers_with_zeros)
def test_connection_with___neg__(
        integer_with_zero: Tuple[Integer, Integer]
) -> None:
    integer, zero = integer_with_zero

    with suppress(OverflowError):
        assert equivalence(integer.is_positive() == (-integer).is_positive(),
                           integer == zero)


@given(strategies.signed_integers_with_zeros)
def test_alternatives(
        integer_with_zero: Tuple[Integer, Integer]
) -> None:
    integer, zero = integer_with_zero

    assert equivalence(integer.is_positive(),
                       not integer.is_negative() and integer != zero)
