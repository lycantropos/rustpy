from hypothesis import given

from rustpy.result import (Result,
                           Ok)
from rustpy.primitive import bool_
from tests.utils import equivalence
from . import strategies


@given(strategies.results)
def test_basic(result: Result) -> None:
    assert isinstance(result.is_ok(), bool_)


@given(strategies.results)
def test_value(result: Result) -> None:
    assert equivalence(result.is_ok(), isinstance(result, Ok))
