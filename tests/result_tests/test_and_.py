from hypothesis import given

from rustpy.result import (Err,
                           Result,
                           Ok)
from . import strategies


@given(strategies.errs, strategies.results)
def test_err(err: Err, result: Result) -> None:
    assert err.and_(result) is err


@given(strategies.oks, strategies.results)
def test_ok(ok: Ok, result: Result) -> None:
    assert ok.and_(result) is result
