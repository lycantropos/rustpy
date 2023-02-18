import typing as _t

import typing_extensions as _te

from .ordered import (Ordered as _Ordered,
                      OrderedWrapper as _OrderedWrapper)


class _Number(_Ordered, _te.Protocol):
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    def __sub__(self, other: _te.Self) -> _te.Self:
        ...


_NumberT = _t.TypeVar('_NumberT',
                      bound=_Number)


class NumberWrapper(_OrderedWrapper[_NumberT]):
    def add(self, other: _te.Self) -> _te.Self:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        return type(self)(self._value + other._value)

    def mul(self, other: _te.Self) -> _te.Self:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        return type(self)(self._value * other._value)

    def sub(self, other: _te.Self) -> _te.Self:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        return type(self)(self._value - other._value)

    @_t.overload
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _t.Any) -> _t.Any:
        ...

    def __add__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value + other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mul__(self, other: _t.Any) -> _t.Any:
        ...

    def __mul__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value * other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __sub__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _t.Any) -> _t.Any:
        ...

    def __sub__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value - other._value)
                if isinstance(other, type(self))
                else NotImplemented)
