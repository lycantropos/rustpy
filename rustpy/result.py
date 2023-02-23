from __future__ import annotations

import typing as _t

import typing_extensions as _te

try:
    from . import _crustpy as _impl
except ImportError:
    from ._rustpy import result as _impl

if _t.TYPE_CHECKING:
    from .option import Option as _Option
    from .primitive import bool_ as _bool

_E = _t.TypeVar('_E')
_E2 = _t.TypeVar('_E2')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Err(_impl.Err, _t.Generic[_E]):
    """Represents the error value."""

    def __init_subclass__(cls, **kwargs: _t.Any) -> _t.NoReturn:
        raise TypeError(f'type \'{cls.__module__}{cls.__qualname__}\' '
                        f'is not an acceptable base type')


class Ok(_impl.Ok, _t.Generic[_T]):
    """Represents the success value."""

    def __init_subclass__(cls, **kwargs: _t.Any) -> _t.NoReturn:
        raise TypeError(f'type \'{cls.__module__}{cls.__qualname__}\' '
                        f'is not an acceptable base type')


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

    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __ge__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        ...
