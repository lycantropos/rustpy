from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.errs, strategies.equatable_pure_maps,
       strategies.equatable_pure_maps)
def test_err(err: Err,
             first_map: Callable[[Any], Any],
             second_map: Callable[[Any], Any]) -> None:
    result = err.map_or_else(first_map, second_map)

    assert result == first_map(err.unwrap_err())


@given(strategies.oks, strategies.equatable_pure_maps,
       strategies.equatable_pure_maps)
def test_ok(ok: Ok,
            first_map: Callable[[Any], Any],
            map_: Callable[[Any], Any]) -> None:
    result = ok.map_or_else(first_map, map_)

    assert result == map_(ok.unwrap())
