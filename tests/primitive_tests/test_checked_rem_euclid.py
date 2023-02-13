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

    result = first.checked_rem_euclid(second)

    assert isinstance(result, (None_, Some))


@given(strategies.integers_pairs)
def test_some(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first.checked_rem_euclid(second)

    assert (result.is_none()
            or (type(first).MIN <= result.unwrap() <= type(first).MAX
                and second != type(first)(0)
                and result.unwrap() == first.rem_euclid(second)))


@given(strategies.integers_pairs)
def test_none(pair: Tuple[Integer, Integer]) -> None:
    first, second = pair

    result = first.checked_rem_euclid(second)

    with (pytest.raises(ZeroDivisionError
                        if second == type(first)(0)
                        else OverflowError)
          if result.is_none()
          else not_raises(OverflowError, ZeroDivisionError)):
        first.rem_euclid(second)
