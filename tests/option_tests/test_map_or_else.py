from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from . import strategies


@given(strategies.nones, strategies.equatable_empty_factories,
       strategies.equatable_pure_maps)
def test_none(none: None_,
              factory: Callable[[], Any],
              map_: Callable[[Any], Any]) -> None:
    result = none.map_or_else(factory, map_)

    assert result == factory()


@given(strategies.somes, strategies.equatable_empty_factories,
       strategies.equatable_pure_maps)
def test_some(some: Some,
              factory: Callable[[], Any],
              map_: Callable[[Any], Any]) -> None:
    result = some.map_or_else(factory, map_)

    assert result == map_(some.unwrap())
