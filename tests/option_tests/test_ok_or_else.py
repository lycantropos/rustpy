from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.nones, strategies.equatable_empty_factories)
def test_none(none: None_, factory: Callable[[], Any]) -> None:
    result = none.ok_or_else(factory)

    assert isinstance(result, Err)
    assert result.unwrap_err() == factory()


@given(strategies.equatable_somes, strategies.equatable_empty_factories)
def test_some(some: Some, factory: Callable[[], Any]) -> None:
    result = some.ok_or_else(factory)

    assert isinstance(result, Ok)
    assert result.unwrap() is some.unwrap()
