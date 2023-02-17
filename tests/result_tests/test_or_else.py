from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Result,
                           Ok)
from . import strategies


@given(strategies.equatable_errs, strategies.results_maps)
def test_err(err: Err, map_: Callable[[Any], Result]) -> None:
    assert err.or_else(map_) == map_(err.unwrap_err())


@given(strategies.equatable_oks, strategies.results_maps)
def test_ok(ok: Ok, map_: Callable[[Any], Result]) -> None:
    assert ok.or_else(map_) is ok
