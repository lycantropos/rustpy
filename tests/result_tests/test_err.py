from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from . import strategies


@given(strategies.equatable_errs)
def test_err(err: Err) -> None:
    result = err.err()

    assert result.is_some()
    assert result.unwrap() is err.unwrap_err()


@given(strategies.equatable_oks)
def test_ok(ok: Ok) -> None:
    result = ok.err()

    assert result.is_none()
