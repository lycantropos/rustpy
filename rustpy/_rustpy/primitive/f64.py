from ctypes import c_float

import typing_extensions as _te

from ._core.float import BaseFloat


@_te.final
class f64(BaseFloat):
    __slots__ = '_value',

    def __init__(self, _value: float) -> None:
        self._value = c_float(_value).value
