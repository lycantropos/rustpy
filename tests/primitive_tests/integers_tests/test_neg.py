from contextlib import suppress

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.signed_integers)
def test_basic(integer: Integer) -> None:
    with suppress(OverflowError):
        result = integer.neg()

        assert isinstance(result, type(integer))


@given(strategies.signed_integers)
def test_connection_with___neg__(integer: Integer) -> None:
    try:
        result = integer.neg()
    except OverflowError as error:
        with pytest.raises(type(error)):
            -integer
    else:
        assert result == -integer
