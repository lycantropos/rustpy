from __future__ import annotations

import abc as _abc
import sys as _sys
import typing as _t

import typing_extensions as _te

from rustpy.option import (None_ as _None,
                           Option as _Option,
                           Some as _Some)
from .bool_ import bool_ as _bool
from .ordered import OrderedWrapper as _OrderedWrapper
from .utils import (floor_division_quotient as _floor_division_quotient,
                    floor_division_remainder as _floor_division_remainder,
                    trunc_division_quotient as _trunc_division_quotient,
                    trunc_division_remainder as _trunc_division_remainder)

if _t.TYPE_CHECKING:
    from rustpy._rustpy.primitive import u32

SIZE_BITS = (_sys.maxsize + 1).bit_length() - 1
assert ((1 << SIZE_BITS) - 1) == _sys.maxsize


def _u32_to_int(value: u32) -> int:
    return value._value


class _BaseInteger(_abc.ABC, _OrderedWrapper[int]):
    BITS: _t.ClassVar[u32]
    MAX: _t.ClassVar[_te.Self]
    MIN: _t.ClassVar[_te.Self]

    def checked_sub(self, other: _te.Self) -> _Option[_te.Self]:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        try:
            return _Some(type(self)(self._value - other._value))
        except OverflowError:
            return _None()

    def div(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(divisor))
        return type(self)(_trunc_division_quotient(self._value,
                                                   divisor._value))

    def div_euclid(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(divisor))
        return type(self)(_floor_division_quotient(self._value,
                                                   divisor._value))

    @_abc.abstractmethod
    def rem(self, divisor: _te.Self) -> _te.Self:
        ...

    def rem_euclid(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(self))
        return type(self)(_floor_division_remainder(self._value,
                                                    divisor._value))

    _value: int

    __module__ = 'rustpy.primitive'
    __slots__ = '_value',

    def __new__(cls, _value: int) -> _te.Self:
        try:
            if not (cls.MIN._value <= _value <= cls.MAX._value):
                raise OverflowError(_value)
        except AttributeError:
            pass
        self = super().__new__(cls)
        self._value = _value
        return self

    @_t.overload
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _t.Any) -> _t.Any:
        ...

    def __add__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value + other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __and__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __and__(self, other: _t.Any) -> _t.Any:
        ...

    def __and__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value & other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    def __bool__(self) -> bool:
        raise TypeError(f'Expected `{_bool.__qualname__}`, '
                        f'found `{type(self).__qualname__}`.')

    @_abc.abstractmethod
    def __invert__(self) -> _te.Self:
        ...

    @_t.overload
    def __lshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __lshift__(self, other: _t.Any) -> _t.Any:
        ...

    def __lshift__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value << _u32_to_int(other))
                if isinstance(other, type(self.BITS))
                else NotImplemented)

    @_t.overload
    def __mod__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mod__(self, other: _t.Any) -> _t.Any:
        ...

    def __mod__(self, other: _t.Any) -> _t.Any:
        return (type(self)(_trunc_division_remainder(self._value,
                                                     other._value))
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mul__(self, other: _t.Any) -> _t.Any:
        ...

    def __mul__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value * other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}({self._value})'

    @_t.overload
    def __rshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __rshift__(self, other: _t.Any) -> _t.Any:
        ...

    def __rshift__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value >> _u32_to_int(other))
                if isinstance(other, type(self.BITS))
                else NotImplemented)

    def __str__(self) -> str:
        return f'{self._value}{type(self).__qualname__}'

    @_t.overload
    def __sub__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _t.Any) -> _t.Any:
        ...

    def __sub__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value - other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __truediv__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __truediv__(self, other: _t.Any) -> _t.Any:
        ...

    def __truediv__(self, other: _t.Any) -> _t.Any:
        return (type(self)(_trunc_division_quotient(self._value, other._value))
                if isinstance(other, type(self))
                else NotImplemented)


class BaseSignedInteger(_BaseInteger):
    def rem(self, divisor: _te.Self) -> _te.Self:
        return (self % divisor
                if ((self < 0) is (divisor < 0))
                else -((-self) % divisor))

    def __invert__(self) -> _te.Self:
        return type(self)(~self._value)

    def __neg__(self) -> _te.Self:
        return type(self)(-self._value)


class BaseUnsignedInteger(_BaseInteger):
    def rem(self, divisor: _te.Self) -> _te.Self:
        return self % divisor

    def __invert__(self) -> _te.Self:
        return type(self)(self.MAX - self._value)


_SignedInteger = _t.TypeVar('_SignedInteger',
                            bound=BaseSignedInteger)


def signed_cls_to_max_value(cls: _t.Type[_SignedInteger]) -> _SignedInteger:
    return cls((1 << (_u32_to_int(cls.BITS) - 1)) - 1)


def signed_cls_to_min_value(cls: _t.Type[_SignedInteger]) -> _SignedInteger:
    return cls(-(1 << (_u32_to_int(cls.BITS) - 1)))


_UnsignedInteger = _t.TypeVar('_UnsignedInteger',
                              bound=BaseUnsignedInteger)


def unsigned_cls_to_max_value(
        cls: _t.Type[_UnsignedInteger]
) -> _UnsignedInteger:
    return cls((1 << _u32_to_int(cls.BITS)) - 1)


def unsigned_cls_to_min_value(
        cls: _t.Type[_UnsignedInteger]
) -> _UnsignedInteger:
    return cls(0)