from typing import Type

import pytest
from hypothesis import given

from rustpy.result import Result
from . import strategies


@given(strategies.results_types)
def test_basic(result_type: Type[Result]) -> None:
    with pytest.raises(TypeError):
        class Fails(result_type):
            pass
