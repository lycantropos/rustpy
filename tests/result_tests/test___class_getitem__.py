from typing import (Any,
                    Type)

from hypothesis import given

from rustpy.result import Result
from tests.utils import GenericAlias
from . import strategies


@given(strategies.results_types, strategies.type_hints)
def test_basic(result_type: Type[Result], type_: Type[Any]) -> None:
    result = result_type[type_]

    assert isinstance(result, GenericAlias)
