from typing import Any

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from . import strategies


@given(strategies.nones, strategies.values)
def test_none(none: None_, value: Any) -> None:
    result = none.unwrap_or(value)

    assert result is value


@given(strategies.somes, strategies.values)
def test_some(some: Some, value: Any) -> None:
    result = some.unwrap_or(value)

    assert result is some.unwrap()