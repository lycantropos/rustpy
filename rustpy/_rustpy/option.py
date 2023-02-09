from __future__ import annotations

import typing as _t

import typing_extensions as _te

from rustpy.primitive import bool_

_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class None_:
    def and_(self, _other: Option[_T]) -> _te.Self:
        return self

    def and_then(self, _function: _t.Callable[[_T], _T2]) -> _te.Self:
        return self

    def is_none(self) -> bool_:
        return bool_(True)

    def is_some(self) -> bool_:
        return bool_(False)

    def map(self, _function: _t.Callable[[_T], _T2]) -> None_:
        return self

    def map_or(self, _default: _T2, _function: _t.Callable[[_T], _T2]) -> _T2:
        return _default

    def map_or_else(self,
                    _default: _t.Callable[[], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        return _default()

    def or_(self, _other: Option[_T]) -> Option[_T]:
        return _other

    def or_else(self,
                _function: _t.Callable[[], Option[_T]]) -> Option[_T]:
        return _function()

    def unwrap(self) -> _t.NoReturn:
        raise ValueError('Called `unwrap` on a `None` value.')

    def unwrap_or(self, _default: _T) -> _T:
        return _default

    def unwrap_or_else(self, _function: _t.Callable[[], _T]) -> _T:
        return _function()


class Some(_t.Generic[_T]):
    def __init__(self, value: _T) -> None:
        self._value = value

    def and_(self, _other: Option[_T]) -> Option[_T]:
        return _other

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        return _function(self._value)

    def is_none(self) -> bool_:
        return bool_(False)

    def is_some(self) -> bool_:
        return bool_(True)

    def or_(self, _other: Option[_T]) -> _te.Self:
        return self

    def or_else(self, _function: _t.Callable[[], Option[_T]]) -> _te.Self:
        return self

    def map(self, _function: _t.Callable[[_T], _T2]) -> Some[_T2]:
        return Some(_function(self._value))

    def map_or(self, _default: _T2, _function: _t.Callable[[_T], _T2]) -> _T2:
        return _function(self._value)

    def map_or_else(self,
                    _default: _t.Callable[[], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        return _function(self._value)

    def unwrap(self) -> _T:
        return self._value

    def unwrap_or(self, _default: _T) -> _T:
        return self._value

    def unwrap_or_else(self, _function: _t.Callable[[], _T]) -> _T:
        return self._value


Option = _t.Union[None_, Some[_T]]
