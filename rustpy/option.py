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

None_.__doc__ = ('Represents absense of value. '
                 'Implements :class:`Option` protocol.')

Some.__doc__ = 'Contains a value. Implements :class:`Option` protocol.'


class Option(_te.Protocol, _t.Generic[_T]):
    """Protocol of an optional value."""

    def and_(self, _other: Option[_T]) -> Option[_T]:
        """Returns self if it :meth:`is_none`, otherwise returns other."""

    def and_then(self,
                 _function: _t.Callable[[_T], Option[_T2]]) -> Option[_T2]:
        """
        Returns self if it :meth:`is_none`,
        otherwise returns the result of given function on the contained value.
        """

    def expect(self, _message: str) -> _T:
        """
        Returns the contained value
        or raises a :class:`ValueError` with given message if none.
        """

    def is_none(self) -> _bool:
        """Checks if the option does not contain a value."""

    def is_some(self) -> _bool:
        """Checks if the option contains a value."""

    def map(self, _function: _t.Callable[[_T], _T2]) -> Option[_T2]:
        """
        Returns self if it :meth:`is_none`,
        otherwise applies given function to a contained value.
        """

    def map_or(self, _default: _T2, _function: _t.Callable[[_T], _T2]) -> _T2:
        """
        Returns given default if self :meth:`is_none`,
        otherwise returns the result of given function on the contained value.
        """

    def map_or_else(self,
                    _default: _t.Callable[[], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        """
        Returns the result of given default function if self :meth:`is_none`,
        otherwise returns the result of given function on the contained value.
        """

    def ok_or(self, _err: _E) -> _Result[_T, _E]:
        """
        Returns the contained value wrapped in :class:`rustpy.result.Ok`
        if self :meth:`is_some`,
        otherwise returns given value wrapped in :class:`rustpy.result.Err`.
        """

    def ok_or_else(self, _function: _t.Callable[[], _E]) -> _Result[_T, _E]:
        """
        Returns the contained value wrapped in :class:`rustpy.result.Ok`
        if self :meth:`is_some`,
        otherwise returns the result of given function
        wrapped in :class:`rustpy.result.Err`.
        """

    def or_(self, _other: Option[_T]) -> Option[_T]:
        """
        Returns self if it :meth:`is_some`, otherwise returns other.
        """

    def or_else(self, _function: _t.Callable[[], Option[_T]]) -> Option[_T]:
        """
        Returns self if it :meth:`is_some`,
        otherwise returns the result of the given function.
        """

    def unwrap(self) -> _T:
        """Returns the contained value."""

    def unwrap_or(self, _default: _T) -> _T:
        """
        Returns the default if self :meth:`is_none`,
        otherwise returns the contained value.
        """

    def unwrap_or_else(self, _function: _t.Callable[[], _T]) -> _T:
        """
        Returns the result of default function if self :meth:`is_none`,
        otherwise returns the contained value.
        """

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
