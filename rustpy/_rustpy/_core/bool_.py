from __future__ import annotations

import typing as _t

import typing_extensions as _te


class bool_:
    _value: bool

    __slots__ = '_value',

    def __new__(cls, _value: bool) -> bool_:
        if not isinstance(_value, bool):
            raise TypeError(type(_value))
        self = super().__new__(cls)
        self._value = _value
        return self

    def __bool__(self) -> bool:
        return self._value

    @_t.overload
    def __eq__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value is other._value)
                if isinstance(other, bool_)
                else NotImplemented)

    @_t.overload
    def __ge__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value >= other._value)
                if isinstance(other, bool_)
                else NotImplemented)

    @_t.overload
    def __gt__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value > other._value)
                if isinstance(other, bool_)
                else NotImplemented)

    @_t.overload
    def __le__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value <= other._value)
                if isinstance(other, bool_)
                else NotImplemented)

    @_t.overload
    def __lt__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value < other._value)
                if isinstance(other, bool_)
                else NotImplemented)

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}({self._value!r})'

    def __str__(self) -> str:
        return 'true' if self._value else 'false'


_T = _t.TypeVar('_T')


def try_construct_bool_(value: _T) -> _t.Union[_T, bool_]:
    return bool_(value) if isinstance(value, bool) else value
