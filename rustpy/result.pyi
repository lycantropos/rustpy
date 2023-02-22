import typing as _t

import typing_extensions as _te

from rustpy.option import Option as _Option
from rustpy.primitive import bool_ as _bool

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

    def err(self) -> _Option[_E]:
        ...

    def expect(self, _message: str) -> _T:
        ...

    def expect_err(self, _message: str) -> _E:
        ...

    def is_err(self) -> _bool:
        ...

    def is_ok(self) -> _bool:
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

    def ok(self) -> _Option[_T]:
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
    def __eq__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __ge__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...


@_te.final
class Err(Result[_t.Any, _E]):
    def __init__(self, _value: _E) -> None:
        ...


@_te.final
class Ok(Result[_T, _t.Any]):
    def __init__(self, _value: _T) -> None:
        ...
