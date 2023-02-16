from typing import Any

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.nones, strategies.equatable_values)
def test_none(none: None_, value: Any) -> None:
    result = none.ok_or(value)

    assert isinstance(result, Err)
    assert result.unwrap_err() is value


@given(strategies.somes, strategies.equatable_values)
def test_some(some: Some, value: Any) -> None:
    result = some.ok_or(value)

    assert isinstance(result, Ok)
    assert result.unwrap() is some.unwrap()
