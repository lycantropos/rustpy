from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.errs, strategies.equatable_pure_maps)
def test_err(err: Err, map_: Callable[[Any], Any]) -> None:
    result = err.map_err(map_)

    assert isinstance(result, Err)
    assert result is not err
    assert result.unwrap_err() == map_(err.unwrap_err())


@given(strategies.oks, strategies.equatable_pure_maps)
def test_ok(ok: Ok, map_: Callable[[Any], Any]) -> None:
    result = ok.map_err(map_)

    assert result is ok
