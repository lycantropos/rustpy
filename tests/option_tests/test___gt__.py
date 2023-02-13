from typing import Tuple

from hypothesis import given

from rustpy.option import Option
from rustpy.primitive import bool_
from tests.utils import (equivalence,
                         implication)
from . import strategies


@given(strategies.comparable_options_pairs)
def test_basic(pair: Tuple[Option, Option]) -> None:
    first, second = pair

    result = first > second

    assert isinstance(result, bool_)


@given(strategies.comparable_options)
def test_irreflexivity(option: Option) -> None:
    assert not option > option


@given(strategies.comparable_options_pairs)
def test_asymmetry(pair: Tuple[Option, Option]) -> None:
    first, second = pair

    assert implication(first > second, not second > first)


@given(strategies.comparable_options_triplets)
def test_transitivity(triplet: Tuple[Option, Option, Option]) -> None:
    first, second, third = triplet

    assert implication(first > second > third, first > third)


@given(strategies.comparable_options_pairs)
def test_equivalents(pair: Tuple[Option, Option]) -> None:
    first, second = pair

    result = first > second

    assert equivalence(result, second < first)
    assert equivalence(result, second <= first != second)
    assert equivalence(result, first >= second != first)
