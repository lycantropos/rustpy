from __future__ import annotations

import typing as _t

import typing_extensions as _te

from ._core.bool_ import (bool_ as _bool,
                          try_construct_bool_ as _try_construct_bool)

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

    def expect(self, _message: str) -> _t.NoReturn:
        raise ValueError(_message)

    def is_none(self) -> _bool:
        return _bool(True)

    def is_some(self) -> _bool:
        return _bool(False)

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
        if not isinstance(_other, (None_, Some)):
            raise TypeError(type(_other))
        return _other

    def or_else(self,
                _function: _t.Callable[[], Option[_T]]) -> Option[_T]:
        result = _function()
        if not isinstance(result, (None_, Some)):
            raise TypeError(type(result))
        return result

    def unwrap(self) -> _t.NoReturn:
        raise ValueError('Called `unwrap` on a `None` value.')

    def unwrap_or(self, _default: _T) -> _T:
        return _default

    def unwrap_or_else(self, _function: _t.Callable[[], _T]) -> _T:
        return _function()

    __module__ = 'rustpy.option'
    __slots__ = ()

    def __init_subclass__(cls, **kwargs: _t.Any) -> _t.NoReturn:
        raise TypeError(f'type \'{cls.__module__}{cls.__qualname__}\' '
                        f'is not an acceptable base type')

    @_t.overload
    def __eq__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (_bool(isinstance(other, None_))
                or (_bool(not isinstance(other, Some))
                    and NotImplemented))

    @_t.overload
    def __ge__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (_bool(isinstance(other, None_))
                or (_bool(not isinstance(other, Some))
                    and NotImplemented))

    @_t.overload
    def __gt__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return _bool(not isinstance(other, (None_, Some))) and NotImplemented

    @_t.overload
    def __le__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return _bool(isinstance(other, (None_, Some))) or NotImplemented

    @_t.overload
    def __lt__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (_bool(not isinstance(other, None_))
                and (_bool(isinstance(other, Some))
                     or NotImplemented))

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}()'


class Some(_t.Generic[_T]):
    def and_(self, _other: Option[_T]) -> Option[_T]:
        if not isinstance(_other, (None_, Some)):
            raise TypeError(type(_other))
        return _other

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        result = _function(self._value)
        if not isinstance(result, (None_, Some)):
            raise TypeError(type(result))
        return result

    def expect(self, _message: str) -> _T:
        return self._value

    def is_none(self) -> _bool:
        return _bool(False)

    def is_some(self) -> _bool:
        return _bool(True)

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

    __module__ = 'rustpy.option'
    __slots__ = '_value',

    def __init__(self, value: _T) -> None:
        self._value = value

    def __init_subclass__(cls, **kwargs: _t.Any) -> _t.NoReturn:
        raise TypeError(f'type \'{cls.__module__}{cls.__qualname__}\' '
                        f'is not an acceptable base type')

    @_t.overload
    def __eq__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (_try_construct_bool(self._value == other._value)
                if isinstance(other, Some)
                else (_bool(not isinstance(other, None_))
                      and NotImplemented))

    @_t.overload
    def __ge__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (_try_construct_bool(self._value >= other._value)
                if isinstance(other, Some)
                else _bool(isinstance(other, None_)) or NotImplemented)

    @_t.overload
    def __gt__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (_try_construct_bool(self._value > other._value)
                if isinstance(other, Some)
                else _bool(isinstance(other, None_)) or NotImplemented)

    @_t.overload
    def __le__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (_try_construct_bool(self._value <= other._value)
                if isinstance(other, Some)
                else _bool(not isinstance(other, None_)) and NotImplemented)

    @_t.overload
    def __lt__(self, other: Option[_T]) -> _bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (_try_construct_bool(self._value < other._value)
                if isinstance(other, Some)
                else _bool(not isinstance(other, None_)) and NotImplemented)

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}({self._value!r})'


Option = _t.Union[None_, Some[_T]]
