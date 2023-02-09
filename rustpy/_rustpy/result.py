from __future__ import annotations

import typing as _t

import typing_extensions as _te

_E = _t.TypeVar('_E')
_E2 = _t.TypeVar('_E2')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Err(_t.Generic[_E]):
    def __init__(self, value: _E) -> None:
        self._value = value

    def and_(self, _other: Result[_T, _E]) -> _te.Self:
        return self

    def and_then(self,
                 _function: _t.Callable[[_T], Result[_T2, _E]]) -> _te.Self:
        return self

    def expect(self, _message: str) -> _t.NoReturn:
        raise ValueError(f'{_message}: {self._value!r}')

    def is_err(self) -> bool:
        return True

    def is_ok(self) -> bool:
        return False

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


class Ok(_t.Generic[_T]):
    def __init__(self, value: _T) -> None:
        self._value = value

    def and_(self, _other: Result[_T, _E]) -> Result[_T, _E]:
        return _other

    def and_then(
            self, _function: _t.Callable[[_T], Result[_T2, _E]]
    ) -> Result[_T2, _E]:
        return _function(self._value)

    def expect(self, _message: str) -> _T:
        return self._value

    def is_err(self) -> bool:
        return False

    def is_ok(self) -> bool:
        return True

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


Result = _t.Union[Ok[_T], Err[_E]]
