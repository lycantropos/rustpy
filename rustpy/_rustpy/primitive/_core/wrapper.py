from __future__ import annotations

import typing as _t

import typing_extensions as _te

from rustpy.primitive.bool_ import bool_

_T = _t.TypeVar('_T')


class _Wrapper(_t.Generic[_T]):
    _value: _T

    __module__ = 'rustpy.primitive'
    __slots__ = '_value',

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value == other._value)
                if isinstance(other, type(self))
                else NotImplemented)
