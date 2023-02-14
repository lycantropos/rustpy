from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first.rem(second)
    except (OverflowError, ZeroDivisionError):
        pass
    else:
        assert isinstance(result, type(first))


@given(strategies.integers_pairs)
def test_connection_with___mod__(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first.rem(second)
    except (OverflowError, ZeroDivisionError) as error:
        with pytest.raises(type(error)):
            first % second
    else:
        assert result == first % second
