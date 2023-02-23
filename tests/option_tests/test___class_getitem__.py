from typing import (Any,
                    Type)

from hypothesis import given

from rustpy.option import Option
from tests.utils import GenericAlias
from . import strategies


@given(strategies.generic_options_types, strategies.type_hints)
def test_basic(option_type: Type[Option], type_: Type[Any]) -> None:
    result = option_type[type_]

    assert isinstance(result, GenericAlias)
