from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.equatable_errs, strategies.equatable_values,
       strategies.equatable_pure_maps)
def test_err(err: Err, value: Any, map_: Callable[[Any], Any]) -> None:
    result = err.map_or(value, map_)

    assert result is value


@given(strategies.equatable_oks, strategies.equatable_values,
       strategies.equatable_pure_maps)
def test_ok(ok: Ok, value: Any, map_: Callable[[Any], Any]) -> None:
    result = ok.map_or(value, map_)

    assert result == map_(ok.unwrap())
