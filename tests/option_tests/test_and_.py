from hypothesis import given

from rustpy.option import (None_,
                           Option,
                           Some)
from . import strategies


@given(strategies.nones, strategies.options)
def test_none(none: None_, option: Option) -> None:
    result = none.and_(option)

    assert result is none


@given(strategies.somes, strategies.options)
def test_some(some: Some, option: Option) -> None:
    result = some.and_(option)

    assert result is option
