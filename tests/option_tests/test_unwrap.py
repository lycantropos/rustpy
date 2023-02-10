import pytest
from hypothesis import given

from rustpy.option import (None_,
                           Some)
from tests.utils import not_raises
from . import strategies


@given(strategies.nones)
def test_none(none: None_) -> None:
    with pytest.raises(ValueError):
        none.unwrap()


@given(strategies.somes)
def test_some(some: Some) -> None:
    with not_raises(BaseException):
        some.unwrap()
