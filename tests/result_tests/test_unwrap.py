import pytest
from hypothesis import given

from rustpy.result import (Err,
                           Ok)
from tests.utils import not_raises
from . import strategies


@given(strategies.equatable_errs)
def test_err(err: Err) -> None:
    with pytest.raises(ValueError):
        err.unwrap()


@given(strategies.equatable_oks)
def test_ok(ok: Ok) -> None:
    with not_raises(BaseException):
        ok.unwrap()
