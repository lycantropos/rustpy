from typing import Tuple

from hypothesis import given

from rustpy.primitive import bool_
from tests.utils import (Primitive,
                         equivalence,
                         implication)
from . import strategies


@given(strategies.finite_primitives_pairs)
def test_basic(pair: Tuple[Primitive, Primitive]) -> None:
    first, second = pair

    result = first == second

    assert isinstance(result, bool_)


@given(strategies.finite_primitives)
def test_reflexivity(primitive: Primitive) -> None:
    assert primitive == primitive


@given(strategies.finite_primitives_pairs)
def test_symmetry(pair: Tuple[Primitive, Primitive]) -> None:
    first, second = pair

    assert equivalence(first == second, second == first)


@given(strategies.finite_primitives_triplets)
def test_transitivity(triplet: Tuple[Primitive, Primitive, Primitive]) -> None:
    first, second, third = triplet

    assert implication(first == second and second == third, first == third)


@given(strategies.finite_primitives_pairs)
def test_connection_with_inequality(pair: Tuple[Primitive, Primitive]) -> None:
    first, second = pair

    assert equivalence(not first == second, first != second)
