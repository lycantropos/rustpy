from contextlib import suppress
from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    with suppress(OverflowError, ZeroDivisionError):
        result = first.div(second)

        assert isinstance(result, type(first))


@given(strategies.integers_pairs)
def test_connection_with___truediv__(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first.div(second)
    except (OverflowError, ZeroDivisionError) as error:
        with pytest.raises(type(error)):
            first / second
    else:
        assert result == first / second
