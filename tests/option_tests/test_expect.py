import pytest
from hypothesis import given

from rustpy.option import (None_,
                           Some)
from tests.utils import not_raises
from . import strategies


@given(strategies.nones, strategies.messages)
def test_none(none: None_, message: str) -> None:
    with pytest.raises(ValueError):
        none.expect(message)


@given(strategies.equatable_somes, strategies.messages)
def test_some(some: Some, message: str) -> None:
    with not_raises(BaseException):
        assert some.expect(message) is some.unwrap()
