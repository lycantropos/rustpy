from __future__ import annotations

import typing as _t

import typing_extensions as _te

from ._core.bool_ import bool_

if _t.TYPE_CHECKING:
    from .result import (Err,
                         Ok)

_E = _t.TypeVar('_E')
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

    def ok_or(self, _err: _E) -> Err[_E]:
        from .result import Err
        return Err(_err)

    def ok_or_else(self, _err: _t.Callable[[], _E]) -> Err[_E]:
        from .result import Err
        return Err(_err())

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

    @_t.overload
    def __eq__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(isinstance(other, None_))
                or (bool_(not isinstance(other, Some))
                    and NotImplemented))

    @_t.overload
    def __ge__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (bool_(isinstance(other, None_))
                or (bool_(not isinstance(other, Some))
                    and NotImplemented))

    @_t.overload
    def __gt__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return bool_(not isinstance(other, (None_, Some))) and NotImplemented

    @_t.overload
    def __le__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return bool_(isinstance(other, (None_, Some))) or NotImplemented

    @_t.overload
    def __lt__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (bool_(not isinstance(other, None_))
                and (bool_(isinstance(other, Some))
                     or NotImplemented))


class Some(_t.Generic[_T]):
    def and_(self, _other: Option[_T]) -> Option[_T]:
        return _other

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        return _function(self._value)

    def is_none(self) -> bool_:
        return bool_(False)

    def is_some(self) -> bool_:
        return bool_(True)

    def ok_or(self, _err: _E) -> Ok[_T]:
        from .result import Ok
        return Ok(self._value)

    def ok_or_else(self, _err: _t.Callable[[], _E]) -> Ok[_T]:
        from .result import Ok
        return Ok(self._value)

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

    def __init__(self, value: _T) -> None:
        self._value = value

    @_t.overload
    def __eq__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value == other._value)
                if isinstance(other, Some)
                else (bool_(not isinstance(other, None_))
                      and NotImplemented))

    @_t.overload
    def __ge__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value >= other._value)
                if isinstance(other, Some)
                else bool_(isinstance(other, None_)) or NotImplemented)

    @_t.overload
    def __gt__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value > other._value)
                if isinstance(other, Some)
                else bool_(isinstance(other, None_)) or NotImplemented)

    @_t.overload
    def __le__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value <= other._value)
                if isinstance(other, Some)
                else bool_(not isinstance(other, None_)) and NotImplemented)

    @_t.overload
    def __lt__(self, other: Option[_T]) -> bool_:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value < other._value)
                if isinstance(other, Some)
                else bool_(not isinstance(other, None_)) and NotImplemented)


Option = _t.Union[None_, Some[_T]]
