from hypothesis import given

from rustpy.option import (None_,
                           Option)
from rustpy.primitive import bool_
from tests.utils import equivalence
from . import strategies


@given(strategies.options)
def test_basic(option: Option) -> None:
    result = option.is_none()

    assert isinstance(result, bool_)


@given(strategies.options)
def test_value(option: Option) -> None:
    assert equivalence(option.is_none(), isinstance(option, None_))
