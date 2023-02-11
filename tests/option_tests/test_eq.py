from hypothesis import given

from rustpy.option import Option
from rustpy.primitive import bool_
from tests.utils import (equivalence,
                         implication)
from . import strategies


@given(strategies.options, strategies.options)
def test_basic(first: Option, second: Option) -> None:
    result = first == second

    assert isinstance(result, bool_)


@given(strategies.options)
def test_reflexivity(option: Option) -> None:
    assert option == option


@given(strategies.options, strategies.options)
def test_symmetry(first: Option, second: Option) -> None:
    assert equivalence(first == second, second == first)


@given(strategies.options, strategies.options, strategies.options)
def test_transitivity(first: Option, second: Option, third: Option) -> None:
    assert implication(first == second and second == third, first == third)


@given(strategies.options, strategies.options)
def test_connection_with_inequality(first: Option, second: Option) -> None:
    assert equivalence(not first == second, first != second)
