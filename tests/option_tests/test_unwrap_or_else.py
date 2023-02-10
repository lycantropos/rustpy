from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from . import strategies


@given(strategies.nones, strategies.values)
def test_none(none: None_, value: Any) -> None:
    result = none.unwrap_or_else(lambda: value)

    assert result is value


@given(strategies.somes, strategies.empty_factories)
def test_some(some: Some, factory: Callable[[], Any]) -> None:
    result = some.unwrap_or_else(factory)

    assert result is some.unwrap()
