from hypothesis import given

from rustpy import primitive as primitive_module
from tests.utils import Primitive
from . import strategies


@given(strategies.comparable_primitives)
def test_basic(primitive: Primitive) -> None:
    result = repr(primitive)

    assert isinstance(result, str)


@given(strategies.losslessly_representable_primitives)
def test_round_trip(primitive: Primitive) -> None:
    result = eval(repr(primitive), vars(primitive_module))

    assert result is not primitive
    assert result == primitive
