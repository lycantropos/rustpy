from hypothesis import given

from rustpy.result import (Err,
                           Result,
                           Ok)
from . import strategies


@given(strategies.equatable_errs, strategies.equatable_results)
def test_err(err: Err, result: Result) -> None:
    assert err.or_(result) is result


@given(strategies.equatable_oks, strategies.equatable_results)
def test_ok(ok: Ok, result: Result) -> None:
    assert ok.or_(result) is ok
