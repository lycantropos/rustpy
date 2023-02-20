import pytest
from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from tests.utils import not_raises
from . import strategies


@given(strategies.equatable_errs, strategies.messages)
def test_err(err: Err, message: str) -> None:
    with not_raises(BaseException):
        assert err.expect_err(message) is err.unwrap_err()


@given(strategies.equatable_oks, strategies.messages)
def test_ok(ok: Ok, message: str) -> None:
    with pytest.raises(ValueError):
        ok.expect_err(message)
