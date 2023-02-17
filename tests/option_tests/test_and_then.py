from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.option import (None_,
                           Option,
                           Some)
from . import strategies


@given(strategies.nones, strategies.options_maps)
def test_none(none: None_, option_map: Callable[[Any], Option]) -> None:
    result = none.and_then(option_map)

    assert result is none


@given(strategies.equatable_somes, strategies.options_maps)
def test_some(some: Some, option_map: Callable[[Any], Option]) -> None:
    result = some.and_then(option_map)

    assert result == option_map(some.unwrap())
