from __future__ import annotations

import typing as _t

import typing_extensions as _te

try:
    from ._crustpy import (Err,
                           Ok)
except ImportError:
    from ._rustpy.result import (Err,
                                 Ok)

_E = _t.TypeVar('_E')
_E2 = _t.TypeVar('_E2')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Result(_te.Protocol, _t.Generic[_T, _E]):
    def and_(self, _other: Result[_T2, _E]) -> Result[_T2, _E]:
        ...

    def and_then(
            self, _other: _t.Callable[[_T], Result[_T2, _E]]
    ) -> Result[_T2, _E]:
        ...

    def expect(self, _message: str) -> _T:
        ...

    def is_err(self) -> bool:
        ...

    def is_ok(self) -> bool:
        ...

    def map(self, _function: _t.Callable[[_T], _T2]) -> Result[_T2, _E]:
        ...

    def map_err(self, _function: _t.Callable[[_E], _E2]) -> Result[_T, _E2]:
        ...

    def map_or(self, _default: _T2, _function: _t.Callable[[_T], _T2]) -> _T2:
        ...

    def map_or_else(self,
                    _default: _t.Callable[[_E], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        ...

    def or_(self, _other: Result[_T, _E2]) -> Result[_T, _E2]:
        ...

    def or_else(self,
                _other: _t.Callable[[_E], Result[_T, _E2]]) -> Result[_T, _E2]:
        ...

    def unwrap(self) -> _T:
        ...

    def unwrap_err(self) -> _E:
        ...

    def unwrap_or(self, _default: _T) -> _T:
        ...

    def unwrap_or_else(self, _function: _t.Callable[[_E], _T]) -> _T:
        ...

    def __bool__(self) -> _t.NoReturn:
        ...

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

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
