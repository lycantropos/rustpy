from typing import Tuple

from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats_pairs)
def test_basic(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first.mul(second)

    assert isinstance(result, type(first))


@given(strategies.finite_floats_pairs)
def test_connection_with___mul__(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first.mul(second)

    assert result == first * second
