from __future__ import annotations

import typing as _t

import typing_extensions as _te

from .primitive import bool_

try:
    from ._crustpy import (None_,
                           Some)
except ImportError:
    from ._rustpy.option import (None_,
                                 Some)

_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Option(_te.Protocol, _t.Generic[_T]):
    def and_(self, _other: Option[_T]) -> Option[_T]:
        ...

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        ...

    def is_none(self) -> bool_:
        ...

    def is_some(self) -> bool_:
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
