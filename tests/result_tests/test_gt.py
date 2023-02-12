from typing import Tuple

from hypothesis import given

from rustpy.result import Result
from rustpy.primitive import bool_
from tests.utils import (equivalence,
                         implication)
from . import strategies


@given(strategies.comparable_results_pairs)
def test_basic(pair: Tuple[Result, Result]) -> None:
    first, second = pair

    result = first > second

    assert isinstance(result, bool_)


@given(strategies.comparable_results)
def test_irreflexivity(result: Result) -> None:
    assert not result > result


@given(strategies.comparable_results_pairs)
def test_asymmetry(pair: Tuple[Result, Result]) -> None:
    first, second = pair

    assert implication(first > second, not second > first)


@given(strategies.comparable_results_triplets)
def test_transitivity(triplet: Tuple[Result, Result, Result]) -> None:
    first, second, third = triplet

    assert implication(first > second > third, first > third)


@given(strategies.comparable_results_pairs)
def test_equivalents(pair: Tuple[Result, Result]) -> None:
    first, second = pair

    result = first > second

    assert equivalence(result, second < first)
    assert equivalence(result, second <= first != second)
    assert equivalence(result, first >= second != first)
