from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from . import strategies


@given(strategies.nones, strategies.equatable_values,
       strategies.equatable_pure_maps)
def test_none(none: None_, value: Any, map_: Callable[[Any], Any]) -> None:
    result = none.map_or(value, map_)

    assert result is value


@given(strategies.somes, strategies.equatable_values,
       strategies.equatable_pure_maps)
def test_some(some: Some, value: Any, map_: Callable[[Any], Any]) -> None:
    result = some.map_or(value, map_)

    assert result == map_(some.unwrap())
