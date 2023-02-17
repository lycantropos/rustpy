from hypothesis import given

from rustpy import (option as option_module,
                    primitive,
                    result as result_module)
from rustpy.result import Result
from . import strategies


@given(strategies.equatable_results)
def test_basic(result: Result) -> None:
    result_ = repr(result)

    assert isinstance(result_, str)


@given(strategies.lossless_representable_results)
def test_round_trip(result: Result) -> None:
    result_ = eval(repr(result), {**vars(primitive), **vars(option_module),
                                  **vars(result_module)})

    assert result_ is not result
    assert result_ == result
