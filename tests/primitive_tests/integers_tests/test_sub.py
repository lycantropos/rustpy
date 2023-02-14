from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first.sub(second)
    except OverflowError:
        pass
    else:
        assert isinstance(result, type(first))


@given(strategies.integers_pairs)
def test_connection_with___sub__(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    try:
        result = first.sub(second)
    except OverflowError:
        with pytest.raises(OverflowError):
            first - second
    else:
        assert result == first - second
