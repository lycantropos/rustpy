from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.errs, strategies.equatable_pure_maps)
def test_err(err: Err, map_: Callable[[Any], Any]) -> None:
    result = err.map(map_)

    assert result is err


@given(strategies.oks, strategies.equatable_pure_maps)
def test_ok(ok: Ok, map_: Callable[[Any], Any]) -> None:
    result = ok.map(map_)

    assert isinstance(result, Ok)
    assert result is not ok
    assert result.unwrap() == map_(ok.unwrap())
