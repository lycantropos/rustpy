from hypothesis import given

from rustpy import (option as option_,
                    primitive,
                    result as result_)
from rustpy.option import Option
from . import strategies


@given(strategies.equatable_options)
def test_basic(option: Option) -> None:
    result = repr(option)

    assert isinstance(result, str)


@given(strategies.lossless_representable_options)
def test_round_trip(option: Option) -> None:
    result = eval(repr(option),
                  {**vars(primitive), **vars(option_), **vars(result_)})

    assert result is not option
    assert result == option
