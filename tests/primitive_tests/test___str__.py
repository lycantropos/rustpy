from hypothesis import given

from tests.utils import Primitive
from . import strategies


@given(strategies.comparable_primitives)
def test_basic(primitive: Primitive) -> None:
    result = str(primitive)

    assert isinstance(result, str)


@given(strategies.losslessly_representable_primitives)
def test_connection_with_repr(primitive: Primitive) -> None:
    result = str(primitive)

    assert result != repr(primitive)
