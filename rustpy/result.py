from __future__ import annotations

import typing as _t

import typing_extensions as _te

try:
    from ._crustpy import (Err,
                           Ok)
except ImportError:
    from ._rustpy.result import (Err,
                                 Ok)

if _t.TYPE_CHECKING:
    from .option import Option as _Option
    from .primitive import bool_ as _bool

_E = _t.TypeVar('_E')
_E2 = _t.TypeVar('_E2')
_T = _t.TypeVar('_T')
_T2 = _t.TypeVar('_T2')

Err.__doc__ = ('Represents the error value. '
               'Implements :class:`Result` protocol.')
Ok.__doc__ = ('Represents the success value. '
              'Implements :class:`Result` protocol.')


class Result(_te.Protocol, _t.Generic[_T, _E]):
    def and_(self, _other: Result[_T2, _E]) -> Result[_T2, _E]:
        """Returns self if it :meth:`is_err`, otherwise returns other."""

    def and_then(
            self, _other: _t.Callable[[_T], Result[_T2, _E]]
    ) -> Result[_T2, _E]:
        """
        Returns self if it :meth:`is_err`,
        otherwise returns the result of given function on the success value.
        """

    def err(self) -> _Option[_E]:
        """
        Returns error value wrapped in :class:`rustpy.option.Some`
        if self :meth:`is_err`, otherwise returns :class:`rustpy.option.None_`.
        """

    def expect(self, _message: str) -> _T:
        """
        Returns the success value
        or raises a :class:`ValueError` with given message if error.
        """

    def expect_err(self, _message: str) -> _E:
        """
        Returns the error value
        or raises a :class:`ValueError` with given message if success.
        """

    def is_err(self) -> _bool:
        """Checks if the result is an error."""

    def is_ok(self) -> _bool:
        """Checks if the result is a success."""

    def map(self, _function: _t.Callable[[_T], _T2]) -> Result[_T2, _E]:
        """
        Returns self if it :meth:`is_err`,
        otherwise applies given function to a success value.
        """

    def map_err(self, _function: _t.Callable[[_E], _E2]) -> Result[_T, _E2]:
        """
        Returns self if it :meth:`is_ok`,
        otherwise applies given function to an error value.
        """

    def map_or(self, _default: _T2, _function: _t.Callable[[_T], _T2]) -> _T2:
        """
        Returns given default if self :meth:`is_err`,
        otherwise returns the result of given function on the success value.
        """

    def map_or_else(self,
                    _default: _t.Callable[[_E], _T2],
                    _function: _t.Callable[[_T], _T2]) -> _T2:
        """
        Returns the result of given default function on the error value
        if self :meth:`is_err`,
        otherwise returns the result of given function on the success value.
        """

    def ok(self) -> _Option[_T]:
        """
        Returns success value wrapped in :class:`rustpy.option.Some`
        if self :meth:`is_ok`, otherwise returns :class:`rustpy.option.None_`.
        """

    def or_(self, _other: Result[_T, _E2]) -> Result[_T, _E2]:
        """Returns self if it :meth:`is_ok`, otherwise returns other."""

    def or_else(self,
                _other: _t.Callable[[_E], Result[_T, _E2]]) -> Result[_T, _E2]:
        """
        Returns self if it :meth:`is_ok`,
        otherwise returns the result of given function on the success value.
        """

    def unwrap(self) -> _T:
        """Returns the success value."""

    def unwrap_err(self) -> _E:
        """Returns the error value."""

    def unwrap_or(self, _default: _T) -> _T:
        """
        Returns the default if self :meth:`is_err`,
        otherwise returns the success value.
        """

    def unwrap_or_else(self, _function: _t.Callable[[_E], _T]) -> _T:
        """
        Returns the result of default function on error value
        if self :meth:`is_err`, otherwise returns the success value.
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
