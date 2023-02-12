from hypothesis import given

from rustpy.result import (Err,
                           Result,
                           Ok)
from . import strategies


@given(strategies.errs, strategies.results)
def test_err(err: Err, result: Result) -> None:
    assert err.or_(result) is result


@given(strategies.oks, strategies.results)
def test_ok(ok: Ok, result: Result) -> None:
    assert ok.or_(result) is ok
