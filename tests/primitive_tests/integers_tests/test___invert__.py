from hypothesis import given

from tests.utils import Integer
from . import strategies


@given(strategies.integers)
def test_basic(integer: Integer) -> None:
    result = ~integer

    assert isinstance(result, type(integer))


@given(strategies.integers)
def test_involution(integer: Integer) -> None:
    assert ~(~integer) == integer
