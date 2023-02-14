from typing import Tuple

import pytest
from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats_pairs)
def test_basic(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first * second

    assert isinstance(result, type(first))


@given(strategies.finite_floats_pairs)
def test_commutativity(pair: Tuple[Float, Float]) -> None:
    first, second = pair

    result = first * second

    assert result == second * first


@given(strategies.finite_floats_with_zeros)
def test_absorbing_element(float_with_zero: Tuple[Float, Float]) -> None:
    float_, zero = float_with_zero

    assert float_ * zero == zero == zero * float_


@given(strategies.finite_floats_with_ones)
def test_neutral_element(float_with_one: Tuple[Float, Float]) -> None:
    float_, one = float_with_one

    assert float_ * one == float_ == one * float_
