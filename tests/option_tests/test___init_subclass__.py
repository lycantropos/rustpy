from typing import Type

import pytest
from hypothesis import given

from rustpy.option import Option
from . import strategies


@given(strategies.options_types)
def test_basic(option_type: Type[Option]) -> None:
    with pytest.raises(TypeError):
        class Fails(option_type):
            pass
