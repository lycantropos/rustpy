from hypothesis import given

from rustpy.result import (Err,
                           Result)
from rustpy.primitive import bool_
from tests.utils import equivalence
from . import strategies


@given(strategies.equatable_results)
def test_basic(result: Result) -> None:
    result = result.is_err()

    assert isinstance(result, bool_)


@given(strategies.equatable_results)
def test_value(result: Result) -> None:
    assert equivalence(result.is_err(), isinstance(result, Err))
