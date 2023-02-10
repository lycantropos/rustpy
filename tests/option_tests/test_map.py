from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Some)
from . import strategies


@given(strategies.nones, strategies.maps)
def test_none(none: None_, map_: Callable[[Any], Any]) -> None:
    result = none.map(map_)

    assert result is none


@given(strategies.somes, strategies.maps)
def test_some(some: Some, map_: Callable[[Any], Any]) -> None:
    result = some.map(map_)

    assert isinstance(result, Some)
    assert result is not some
