from __future__ import annotations

import typing as _t

import typing_extensions as _te

try:
    from ._crustpy import (None_,
                           Some)
except ImportError:
    from ._rustpy.option import (None_,
                                 Some)

if _t.TYPE_CHECKING:
    from .primitive import bool_ as _bool
    from .result import Result as _Result

_E = _t.TypeVar('_E')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Option(_te.Protocol, _t.Generic[_T]):
    def and_(self, _other: Option[_T]) -> Option[_T]:
        ...

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        ...

    def is_none(self) -> _bool:
        ...

    def is_some(self) -> _bool:
        ...

    def ok_or(self, _err: _E) -> _Result[_T, _E]:
        ...

    def ok_or_else(self, _err: _t.Callable[[], _E]) -> _Result[_T, _E]:
        ...

    def or_(self, _other: Option[_T]) -> Option[_T]:
        ...

    def or_else(self, _function: _t.Callable[[], Option[_T]]) -> Option[_T]:
        ...

    def map(self, _function: _t.Callable[[_T], _T2]) -> Some[_T2]:
        ...

    def map_or(self, _default: _T2, _function: _t.Callable[[_T], _T2]) -> _T2:
        ...

    def map_or_else(self,
                    _default: _t.Callable[[], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        ...

    def unwrap(self) -> _T:
        ...

    def unwrap_or(self, _default: _T) -> _T:
        ...

    def unwrap_or_else(self, _function: _t.Callable[[], _T]) -> _T:
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
