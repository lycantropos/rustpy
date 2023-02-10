from __future__ import annotations

import typing as _t

import typing_extensions as _te


@_te.final
class bool_:
    _value: bool

    __slots__ = '_value',

    def __new__(cls, _value: bool) -> bool_:
        if not isinstance(_value, (bool, bool_)):
            raise TypeError(type(_value))
        self = super().__new__(cls)
        self._value = bool(_value)
        return self

    def __bool__(self) -> bool:
        return self._value

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value is other._value)
                if isinstance(other, bool_)
                else NotImplemented)
