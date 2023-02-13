from typing import Tuple

import pytest
from hypothesis import given

from rustpy.option import (None_,
                           Some)
from tests.utils import (Integer,
                         not_raises)
from . import strategies


@given(strategies.integers_pairs)
def test_basic(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first.checked_add(second)

    assert isinstance(result, (None_, Some))


@given(strategies.integers_pairs)
def test_some(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first.checked_add(second)

    assert (result.is_none()
            or (type(first).MIN <= result.unwrap() <= type(first).MAX
                and result.unwrap() == first.add(second)))


@given(strategies.integers_pairs)
def test_none(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first.checked_add(second)

    with (pytest.raises if result.is_none() else not_raises)(OverflowError):
        first.add(second)
