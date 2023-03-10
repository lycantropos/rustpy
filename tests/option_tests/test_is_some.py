from hypothesis import given

from rustpy.option import (Option,
                           Some)
from rustpy.primitive import bool_
from tests.utils import equivalence
from . import strategies


@given(strategies.equatable_options)
def test_basic(option: Option) -> None:
    result = option.is_some()

    assert isinstance(result, bool_)


@given(strategies.equatable_options)
def test_value(option: Option) -> None:
    assert equivalence(option.is_some(), isinstance(option, Some))


@given(strategies.equatable_options)
def test_connection_with_is_none(option: Option) -> None:
    assert equivalence(bool(option.is_some()), not option.is_none())
