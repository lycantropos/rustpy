from hypothesis import given

from tests.utils import Float
from . import strategies


@given(strategies.finite_floats)
def test_round_trip(float_: Float) -> None:
    result = float_.from_le_bytes(float_.to_le_bytes())

    assert result is not float_
    assert result == float_
