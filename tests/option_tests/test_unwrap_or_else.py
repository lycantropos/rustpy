from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from . import strategies


@given(strategies.nones, strategies.equatable_empty_factories)
def test_none(none: None_, factory: Callable[[], Any]) -> None:
    result = none.unwrap_or_else(factory)

    assert result == factory()


@given(strategies.equatable_somes, strategies.equatable_empty_factories)
def test_some(some: Some, factory: Callable[[], Any]) -> None:
    result = some.unwrap_or_else(factory)

    assert result is some.unwrap()
