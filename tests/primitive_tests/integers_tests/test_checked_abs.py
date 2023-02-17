import pytest
from hypothesis import given

from rustpy.option import (None_,
                           Some)
from tests.utils import (Integer,
                         not_raises)
from . import strategies


@given(strategies.signed_integers)
def test_basic(integer: Integer) -> None:
    result = integer.checked_abs()

    assert isinstance(result, (None_, Some))


@given(strategies.signed_integers)
def test_some(integer: Integer) -> None:
    result = integer.checked_abs()

    assert (result.is_none()
            or (type(integer).MIN <= result.unwrap() <= type(integer).MAX
                and result.unwrap() == integer.abs()))


@given(strategies.signed_integers)
def test_none(integer: Integer) -> None:
    result = integer.checked_abs()

    with (pytest.raises if result.is_none() else not_raises)(OverflowError):
        integer.abs()
