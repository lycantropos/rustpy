from typing import Tuple

from hypothesis import given

from rustpy.primitive import bool_
from tests.utils import (Primitive,
                         equivalence,
                         implication)
from . import strategies


@given(strategies.comparable_primitives_pairs)
def test_basic(pair: Tuple[Primitive, Primitive]) -> None:
    first, second = pair

    result = first < second

    assert isinstance(result, bool_)


@given(strategies.comparable_primitives)
def test_irreflexivity(primitive: Primitive) -> None:
    assert not primitive < primitive


@given(strategies.comparable_primitives_pairs)
def test_asymmetry(pair: Tuple[Primitive, Primitive]) -> None:
    first, second = pair

    assert implication(first < second, not second < first)


@given(strategies.comparable_primitives_triplets)
def test_transitivity(triplet: Tuple[Primitive, Primitive, Primitive]) -> None:
    first, second, third = triplet

    assert implication(first < second < third, first < third)


@given(strategies.comparable_primitives_pairs)
def test_equivalents(pair: Tuple[Primitive, Primitive]) -> None:
    first, second = pair

    result = first < second

    assert equivalence(result, second > first)
    assert equivalence(result, second >= first != second)
    assert equivalence(result, first <= second != first)
