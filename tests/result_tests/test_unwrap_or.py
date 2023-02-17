from typing import Any

from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.equatable_errs, strategies.equatable_values)
def test_err(err: Err, value: Any) -> None:
    assert err.unwrap_or(value) is value


@given(strategies.equatable_oks, strategies.equatable_values)
def test_ok(ok: Ok, value: Any) -> None:
    assert ok.unwrap_or(value) is ok.unwrap()
