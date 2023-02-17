from typing import (Any,
                    Callable)

from hypothesis import given

from rustpy.result import (Err,
                           Result,
                           Ok)
from . import strategies


@given(strategies.equatable_errs, strategies.results_maps)
def test_err(err: Err, result_map: Callable[[Any], Result]) -> None:
    assert err.and_then(result_map) is err


@given(strategies.equatable_oks, strategies.results_maps)
def test_ok(ok: Ok, result_map: Callable[[Any], Result]) -> None:
    assert ok.and_then(result_map) == result_map(ok.unwrap())
