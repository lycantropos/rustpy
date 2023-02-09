from __future__ import annotations

import sys
import typing as _t
from abc import (ABC,
                 abstractmethod)
from ctypes import c_float

import typing_extensions as _te

from rustpy._rustpy.utils import (floor_division_quotient,
                                  floor_division_remainder,
                                  trunc_division_quotient,
                                  trunc_division_remainder)

if _t.TYPE_CHECKING:
    from rustpy.option import Option

SIZE_BITS = (sys.maxsize + 1).bit_length() - 1
assert ((1 << SIZE_BITS) - 1) == sys.maxsize


@_te.final
class bool_:
    _value: bool

    __slots__ = '_value',

    def __new__(cls, _value: bool) -> bool_:
        if not isinstance(_value, (bool, bool_)):
            raise TypeError(type(_value))
        self = super().__new__(cls)
        self._value = bool(_value)
        return self

    def __bool__(self) -> bool:
        return self._value

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value is other._value)
                if isinstance(other, bool_)
                else NotImplemented)


class _BaseFloat(ABC):
    _value: float

    def __bool__(self) -> bool:
        raise TypeError(f'Expected `{bool_.__qualname__}`, '
                        f'found `{type(self).__qualname__}`.')

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value == other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __ge__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value >= other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value > other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __le__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value <= other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value < other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    def __str__(self) -> str:
        return f'{self._value}{type(self).__qualname__}'


@_te.final
class f32(_BaseFloat):
    __slots__ = '_value',

    def __init__(self, _value: float) -> None:
        self._value = c_float(_value).value


@_te.final
class f64(_BaseFloat):
    __slots__ = '_value',

    def __init__(self, _value: float) -> None:
        self._value = _value


class _BaseInteger(ABC):
    BITS: _t.ClassVar[u32]
    MAX: _t.ClassVar[_te.Self]
    MIN: _t.ClassVar[_te.Self]

    def checked_sub(self, other: _te.Self) -> Option[_te.Self]:
        from rustpy.option import (None_,
                                   Some)

        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        try:
            return Some(type(self)(self._value - other._value))
        except OverflowError:
            return None_()

    def div(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(divisor))
        return type(self)(trunc_division_quotient(self._value, divisor._value))

    def div_euclid(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(divisor))
        return type(self)(floor_division_quotient(self._value, divisor._value))

    @abstractmethod
    def rem(self, divisor: _te.Self) -> _te.Self:
        ...

    def rem_euclid(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(self))
        return type(self)(floor_division_remainder(self._value,
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
        raise TypeError(f'Expected `{bool_.__qualname__}`, '
                        f'found `{type(self).__qualname__}`.')

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __eq__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value == other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __ge__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    def __ge__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value >= other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __gt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value > other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @abstractmethod
    def __invert__(self) -> _te.Self:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    def __le__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value <= other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __lshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __lshift__(self, other: _t.Any) -> _t.Any:
        ...

    def __lshift__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value << other._value)
                if isinstance(other, u32)
                else NotImplemented)

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    def __lt__(self, other: _t.Any) -> _t.Any:
        return (bool_(self._value < other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __mod__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mod__(self, other: _t.Any) -> _t.Any:
        ...

    def __mod__(self, other: _t.Any) -> _t.Any:
        return (type(self)(trunc_division_remainder(self._value, other._value))
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
        return (type(self)(self._value >> other._value)
                if isinstance(other, u32)
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
        return (type(self)(trunc_division_quotient(self._value, other._value))
                if isinstance(other, type(self))
                else NotImplemented)


class _BaseSignedInteger(_BaseInteger):
    def rem(self, divisor: _te.Self) -> _te.Self:
        return (self % divisor
                if ((self < 0) is (divisor < 0))
                else -((-self) % divisor))

    def __invert__(self) -> _te.Self:
        return type(self)(~self._value)

    def __neg__(self) -> _te.Self:
        return type(self)(-self._value)


class _BaseUnsignedInteger(_BaseInteger):
    def rem(self, divisor: _te.Self) -> _te.Self:
        return self % divisor

    def __invert__(self) -> _te.Self:
        return type(self)(self.MAX - self._value)


_SignedInteger = _t.TypeVar('_SignedInteger',
                            bound=_BaseSignedInteger)


def _signed_cls_to_max_value(cls: _t.Type[_SignedInteger]) -> _SignedInteger:
    return cls((1 << (cls.BITS._value - 1)) - 1)


def _signed_cls_to_min_value(cls: _t.Type[_SignedInteger]) -> _SignedInteger:
    return cls(-(1 << (cls.BITS._value - 1)))


_UnsignedInteger = _t.TypeVar('_UnsignedInteger',
                              bound=_BaseUnsignedInteger)


def _unsigned_cls_to_max_value(
        cls: _t.Type[_UnsignedInteger]
) -> _UnsignedInteger:
    return cls((1 << cls.BITS._value) - 1)


@_te.final
class u32(_BaseUnsignedInteger):
    pass


u32.BITS = u32(32)
u32.MAX = _unsigned_cls_to_max_value(u32)
u32.MIN = u32(0)


@_te.final
class i8(_BaseSignedInteger):
    pass


i8.BITS = u32(8)
i8.MAX = _signed_cls_to_max_value(i8)
i8.MIN = _signed_cls_to_min_value(i8)


@_te.final
class i16(_BaseSignedInteger):
    pass


i16.BITS = u32(16)
i16.MAX = _signed_cls_to_max_value(i16)
i16.MIN = _signed_cls_to_min_value(i16)


@_te.final
class i32(_BaseSignedInteger):
    pass


i32.BITS = u32(32)
i32.MAX = _signed_cls_to_max_value(i32)
i32.MIN = _signed_cls_to_min_value(i32)


@_te.final
class i64(_BaseSignedInteger):
    pass


i64.BITS = u32(64)
i64.MAX = _signed_cls_to_max_value(i64)
i64.MIN = _signed_cls_to_min_value(i64)


@_te.final
class i128(_BaseSignedInteger):
    pass


i128.BITS = u32(128)
i128.MAX = _signed_cls_to_max_value(i128)
i128.MIN = _signed_cls_to_min_value(i128)


@_te.final
class isize(_BaseSignedInteger):
    pass


isize.BITS = u32(SIZE_BITS)
isize.MAX = _signed_cls_to_max_value(isize)
isize.MIN = _signed_cls_to_min_value(isize)


@_te.final
class u8(_BaseUnsignedInteger):
    pass


u8.BITS = u32(8)
u8.MAX = _unsigned_cls_to_max_value(u8)
u8.MIN = u8(0)


@_te.final
class u16(_BaseUnsignedInteger):
    pass


u16.BITS = u32(16)
u16.MAX = _unsigned_cls_to_max_value(u16)
u16.MIN = u16(0)


@_te.final
class u64(_BaseUnsignedInteger):
    pass


u64.BITS = u32(64)
u64.MAX = _unsigned_cls_to_max_value(u64)
u64.MIN = u64(0)


@_te.final
class u128(_BaseUnsignedInteger):
    pass


u128.BITS = u32(128)
u128.MAX = _unsigned_cls_to_max_value(u128)
u128.MIN = u128(0)


@_te.final
class usize(_BaseUnsignedInteger):
    pass


usize.BITS = u32(SIZE_BITS)
usize.MAX = _unsigned_cls_to_max_value(usize)
usize.MIN = usize(0)
