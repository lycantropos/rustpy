from __future__ import annotations

import typing as _t

import typing_extensions as _te

from ._core.bool_ import bool_ as _bool
from .option import (None_ as _None,
                     Some as _Some)

_E = _t.TypeVar('_E')
_E2 = _t.TypeVar('_E2')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Err(_t.Generic[_E]):
    def and_(self, _other: Result[_T, _E]) -> _te.Self:
        return self

    def and_then(self,
                 _function: _t.Callable[[_T], Result[_T2, _E]]) -> _te.Self:
        return self

    def err(self) -> _Some[_E]:
        return _Some(self._value)

    def expect(self, _message: str) -> _t.NoReturn:
        raise ValueError(f'{_message}: {self._value!r}')

    def is_err(self) -> _bool:
        return _bool(True)

    def is_ok(self) -> _bool:
        return _bool(False)

    def map(self, _function: _t.Callable[[_T], _T2]) -> _te.Self:
        return self

    def map_err(self, _function: _t.Callable[[_E], _E2]) -> Err[_E2]:
        return Err(_function(self._value))

    def map_or(self,
               _default: _T2,
               _function: _t.Callable[[_T], _T2]) -> _T2:
        return _default

    def map_or_else(self,
                    _default: _t.Callable[[_E], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        return _default(self._value)

    def ok(self) -> _None:
        return _None()

    def or_(self, _other: Result[_T, _E]) -> Result[_T, _E]:
        return _other

    def or_else(
            self, _function: _t.Callable[[_E], Result[_T, _E2]]
    ) -> Result[_T, _E2]:
        return _function(self._value)

    def unwrap(self) -> _t.NoReturn:
        raise ValueError('Called `unwrap` on an `Err` value: '
                         f'{self._value!r}.')

    def unwrap_or(self, _default: _T) -> _T:
        return _default

    def unwrap_err(self) -> _E:
        return self._value

    def unwrap_or_else(self, _function: _t.Callable[[_E], _T]) -> _T:
        return _function(self._value)

    def __init__(self, value: _E) -> None:
        self._value = value

    @_t.overload
    def __eq__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value == other._value))
                if isinstance(other, Err)
                else (_bool(not isinstance(other, Ok))
                      and NotImplemented))

    @_t.overload
    def __ge__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value >= other._value))
                if isinstance(other, Err)
                else _bool(isinstance(other, Ok)) or NotImplemented)

    @_t.overload
    def __gt__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value > other._value))
                if isinstance(other, Err)
                else _bool(isinstance(other, Ok)) or NotImplemented)

    @_t.overload
    def __le__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value <= other._value))
                if isinstance(other, Err)
                else _bool(not isinstance(other, Ok)) and NotImplemented)

    @_t.overload
    def __lt__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value < other._value))
                if isinstance(other, Err)
                else _bool(not isinstance(other, Ok)) and NotImplemented)


class Ok(_t.Generic[_T]):
    def and_(self, _other: Result[_T, _E]) -> Result[_T, _E]:
        return _other

    def and_then(
            self, _function: _t.Callable[[_T], Result[_T2, _E]]
    ) -> Result[_T2, _E]:
        return _function(self._value)

    def err(self) -> _None:
        return _None()

    def expect(self, _message: str) -> _T:
        return self._value

    def is_err(self) -> _bool:
        return _bool(False)

    def is_ok(self) -> _bool:
        return _bool(True)

    def map(self, _function: _t.Callable[[_T], _T2]) -> Ok[_T2]:
        return Ok(_function(self._value))

    def map_err(self, _function: _t.Callable[[_E], _E2]) -> _te.Self:
        return self

    def map_or(self,
               _default: _T2,
               _function: _t.Callable[[_T], _T2]) -> _T2:
        return _function(self._value)

    def map_or_else(self,
                    _default: _t.Callable[[_E], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        return _function(self._value)

    def ok(self) -> _Some[_T]:
        return _Some(self._value)

    def or_(self, _other: Result[_T, _E]) -> _te.Self:
        return self

    def or_else(self,
                _function: _t.Callable[[_E], Result[_T, _E2]]) -> _te.Self:
        return self

    def unwrap(self) -> _T:
        return self._value

    def unwrap_err(self) -> _t.NoReturn:
        raise ValueError('Called `unwrap_err` on an `Ok` value: '
                         f'{self._value!r}.')

    def unwrap_or(self, _default: _T) -> _T:
        return self._value

    def unwrap_or_else(self, _function: _t.Callable[[_E], _T]) -> _T:
        return self._value

    def __init__(self, value: _T) -> None:
        self._value = value

    @_t.overload
    def __eq__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value == other._value))
                if isinstance(other, Ok)
                else (_bool(not isinstance(other, Err))
                      and NotImplemented))

    @_t.overload
    def __ge__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value >= other._value))
                if isinstance(other, Ok)
                else _bool(not isinstance(other, Err)) and NotImplemented)

    @_t.overload
    def __gt__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value > other._value))
                if isinstance(other, Ok)
                else _bool(not isinstance(other, Err)) and NotImplemented)

    @_t.overload
    def __le__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value <= other._value))
                if isinstance(other, Ok)
                else _bool(isinstance(other, Err)) or NotImplemented)

    @_t.overload
    def __lt__(self, other: Result[_T, _E]) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (_bool(bool(self._value < other._value))
                if isinstance(other, Ok)
                else _bool(isinstance(other, Err)) or NotImplemented)


Result = _t.Union[Ok[_T], Err[_E]]
