from hypothesis import given

from rustpy.option import (None_,
                           Option,
                           Some)
from . import strategies


@given(strategies.nones, strategies.equatable_options)
def test_none(none: None_, option: Option) -> None:
    result = none.or_(option)

    assert result is option


@given(strategies.equatable_somes, strategies.equatable_options)
def test_some(some: Some, option: Option) -> None:
    result = some.or_(option)

    assert result is some
