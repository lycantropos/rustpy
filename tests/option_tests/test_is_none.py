from hypothesis import given

from rustpy.option import (None_,
                           Option)
from rustpy.primitive import bool_
from tests.utils import equivalence
from . import strategies


@given(strategies.equatable_options)
def test_basic(option: Option) -> None:
    result = option.is_none()

    assert isinstance(result, bool_)


@given(strategies.equatable_options)
def test_value(option: Option) -> None:
    assert equivalence(option.is_none(), isinstance(option, None_))


@given(strategies.equatable_options)
def test_connection_with_is_some(option: Option) -> None:
    assert equivalence(bool(option.is_none()), not option.is_some())
