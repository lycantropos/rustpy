from typing import Callable

from hypothesis import given

from rustpy.option import (None_,
                           Option,
                           Some)
from . import strategies


@given(strategies.nones, strategies.options_empty_factories)
def test_none(none: None_, factory: Callable[[], Option]) -> None:
    result = none.or_else(factory)

    assert result == factory()


@given(strategies.somes, strategies.options_empty_factories)
def test_some(some: Some, factory: Callable[[], Option]) -> None:
    result = some.or_else(factory)

    assert result is some
