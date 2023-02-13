from hypothesis import given

from rustpy.result import Result
from rustpy.primitive import bool_
from tests.utils import (equivalence,
                         implication)
from . import strategies


@given(strategies.results, strategies.results)
def test_basic(first: Result, second: Result) -> None:
    result = first == second

    assert isinstance(result, bool_)


@given(strategies.results)
def test_reflexivity(result: Result) -> None:
    assert result == result


@given(strategies.results, strategies.results)
def test_symmetry(first: Result, second: Result) -> None:
    assert equivalence(first == second, second == first)


@given(strategies.results, strategies.results, strategies.results)
def test_transitivity(first: Result, second: Result, third: Result) -> None:
    assert implication(first == second and second == third, first == third)


@given(strategies.results, strategies.results)
def test_connection_with_inequality(first: Result, second: Result) -> None:
    assert equivalence(not first == second, first != second)
