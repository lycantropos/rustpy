from contextlib import suppress
from typing import Tuple

from hypothesis import given

from rustpy.primitive import u32
from tests.utils import Integer
from . import strategies


@given(strategies.integers, strategies.u32s)
def test_basic(base: Integer, shift: u32) -> None:
    result = base << shift

    assert isinstance(result, type(base))


@given(strategies.zero_integers, strategies.u32s)
def test_left_absorbing_element(zero: Integer, shift: u32) -> None:
    result = zero << shift

    assert result == zero


@given(strategies.integers, strategies.u32_zeros)
def test_right_neutral_element(base: Integer, zero: u32) -> None:
    result = base << zero

    assert result == base


@given(strategies.integers_pairs, strategies.u32s)
def test___add___base(bases_pair: Tuple[Integer, Integer], shift: u32) -> None:
    first_base, second_base = bases_pair

    with suppress(OverflowError):
        result = (first_base + second_base) << shift

        assert result == (first_base << shift) + (second_base << shift)


@given(strategies.integers_pairs, strategies.u32s)
def test___mul___base(bases_pair: Tuple[Integer, Integer], shift: u32) -> None:
    first_base, second_base = bases_pair

    with suppress(OverflowError):
        result = (first_base * second_base) << shift

        assert result == (first_base << shift) * second_base
        assert result == first_base * (second_base << shift)
