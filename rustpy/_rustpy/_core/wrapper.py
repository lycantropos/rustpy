from __future__ import annotations

import typing as _t

import typing_extensions as _te

from .bool_ import bool_ as _bool

_T = _t.TypeVar('_T')


class Wrapper(_t.Generic[_T]):
    _value: _T

    __module__ = 'rustpy.primitive'
    __slots__ = '_value',

    def __init__(self, _value: _T) -> None:
        self._value = _value

    def __bool__(self) -> _t.NoReturn:
        raise TypeError(f'Expected `{_bool.__qualname__}`, '
                        f'found `{type(self).__qualname__}`.')

    @_t.overload
    def __eq__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (_bool(self._value == other._value)
                if isinstance(other, type(self))
                else NotImplemented)
