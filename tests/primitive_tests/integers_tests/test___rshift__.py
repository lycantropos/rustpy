from hypothesis import given

from rustpy.primitive import u32
from tests.utils import Integer
from . import strategies


@given(strategies.integers, strategies.u32s)
def test_basic(base: Integer, shift: u32) -> None:
    result = base >> shift

    assert isinstance(result, type(base))


@given(strategies.zero_integers, strategies.u32s)
def test_left_absorbing_element(zero: Integer, shift: u32) -> None:
    result = zero >> shift

    assert result == zero


@given(strategies.integers, strategies.u32_zeros)
def test_right_neutral_element(base: Integer, zero: u32) -> None:
    result = base >> zero

    assert result == base
