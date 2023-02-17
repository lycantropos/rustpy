from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.equatable_errs, strategies.equatable_pure_maps)
def test_err(err: Err, map_: Callable[[Any], Any]) -> None:
    assert err.unwrap_or_else(map_) == map_(err.unwrap_err())


@given(strategies.equatable_oks, strategies.equatable_pure_maps)
def test_ok(ok: Ok, map_: Callable[[Any], Any]) -> None:
    assert ok.unwrap_or_else(map_) is ok.unwrap()
