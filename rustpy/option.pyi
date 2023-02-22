import typing as _t

import typing_extensions as _te

from rustpy.primitive import bool_ as _bool
from rustpy.result import Result

_E = _t.TypeVar('_E')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')


class Option(_te.Protocol, _t.Generic[_T]):
    def and_(self, _other: Option[_T]) -> Option[_T]:
        ...

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        ...

    def expect(self, _message: str) -> _T:
        ...

    def is_none(self) -> _bool:
        ...

    def is_some(self) -> _bool:
        ...

    def ok_or(self, _err: _E) -> Result[_T, _E]:
        ...

    def ok_or_else(self, _err: _t.Callable[[], _E]) -> Result[_T, _E]:
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
class None_(Option[_t.Any]):
    pass


@_te.final
class Some(Option[_T]):
    def __init__(self, _value: _T) -> None:
        ...
