from __future__ import annotations

import typing as _t

import typing_extensions as _te

from .bool_ import bool_ as _bool
from .wrapper import Wrapper as _Wrapper


class Ordered(_te.Protocol):
    @_t.overload
    def __ge__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        ...


_OrderedT = _t.TypeVar('_OrderedT',
                       bound=Ordered)


class OrderedWrapper(_Wrapper[_OrderedT]):
    @_t.overload
    def __ge__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (_bool(self._value >= other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __gt__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (_bool(self._value > other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __le__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (_bool(self._value <= other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __lt__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (_bool(self._value < other._value)
                if isinstance(other, type(self))
                else NotImplemented)
