import typing as _t

import typing_extensions as _te

from rustpy.option import Option as _Option


@_te.final
class bool_:
    def as_(self, cls: _t.Type[_CastableFromBool]) -> _CastableFromBool:
        ...

    def __init__(self, _value: bool) -> None:
        ...


class _BaseFloat(_te.Protocol):
    DIGITS: _t.ClassVar[u32] = ...
    EPSILON: _t.ClassVar[_te.Self] = ...
    INFINITY: _t.ClassVar[_te.Self] = ...
    MANTISSA_DIGITS: _t.ClassVar[u32] = ...
    MAX: _t.ClassVar[_te.Self] = ...
    MAX_10_EXP: _t.ClassVar[i32] = ...
    MAX_EXP: _t.ClassVar[i32] = ...
    MIN: _t.ClassVar[_te.Self] = ...
    MIN_10_EXP: _t.ClassVar[i32] = ...
    MIN_EXP: _t.ClassVar[i32] = ...
    MIN_POSITIVE: _t.ClassVar[_te.Self] = ...
    NAN: _t.ClassVar[_te.Self] = ...
    NEG_INFINITY: _t.ClassVar[_te.Self] = ...
    RADIX: _t.ClassVar[u32] = ...

    @classmethod
    def from_be_bytes(cls, _bytes: bytes) -> _te.Self:
        ...

    @classmethod
    def from_le_bytes(cls, _bytes: bytes) -> _te.Self:
        ...

    @classmethod
    def from_ne_bytes(cls, _bytes: bytes) -> _te.Self:
        ...

    def abs(self) -> _te.Self:
        ...

    def add(self, other: _te.Self) -> _te.Self:
        ...

    def as_(self, cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
        ...

    def ceil(self) -> _te.Self:
        ...

    def div(self, divisor: _te.Self) -> _te.Self:
        ...

    def div_euclid(self, divisor: _te.Self) -> _te.Self:
        ...

    def floor(self) -> _te.Self:
        ...

    def fract(self) -> _te.Self:
        ...

    def is_finite(self) -> bool_:
        ...

    def is_infinite(self) -> bool_:
        ...

    def is_nan(self) -> bool_:
        ...

    def mul(self, other: _te.Self) -> _te.Self:
        ...

    def neg(self) -> _te.Self:
        ...

    def rem(self, divisor: _te.Self) -> _te.Self:
        ...

    def rem_euclid(self, divisor: _te.Self) -> _te.Self:
        ...

    def round(self) -> _te.Self:
        ...

    def sub(self, other: _te.Self) -> _te.Self:
        ...

    def to_be_bytes(self) -> bytes:
        ...

    def to_le_bytes(self) -> bytes:
        ...

    def to_ne_bytes(self) -> bytes:
        ...

    def trunc(self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _t.Any) -> _t.Any:
        ...

    def __bool__(self) -> _t.NoReturn:
        ...

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    def __float__(self) -> float:
        ...

    @_t.overload
    def __ge__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __init__(self, _value: float) -> None:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __mod__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mod__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mul__(self, other: _t.Any) -> _t.Any:
        ...

    def __neg__(self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __truediv__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __truediv__(self, other: _t.Any) -> _t.Any:
        ...


@_te.final
class f32(_BaseFloat):
    pass


@_te.final
class f64(_BaseFloat):
    pass


class _BaseInteger(_te.Protocol):
    BITS: _t.ClassVar[u32] = ...
    MAX: _t.ClassVar[_te.Self] = ...
    MIN: _t.ClassVar[_te.Self] = ...

    @classmethod
    def from_be_bytes(cls, _bytes: bytes) -> _te.Self:
        ...

    @classmethod
    def from_le_bytes(cls, _bytes: bytes) -> _te.Self:
        ...

    @classmethod
    def from_ne_bytes(cls, _bytes: bytes) -> _te.Self:
        ...

    def add(self, other: _te.Self) -> _te.Self:
        ...

    def as_(self, cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
        ...

    def checked_add(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def checked_div(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def checked_div_euclid(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def checked_mul(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def checked_rem(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def checked_rem_euclid(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def checked_sub(self, other: _te.Self) -> _Option[_te.Self]:
        ...

    def div(self, divisor: _te.Self) -> _te.Self:
        ...

    def div_euclid(self, divisor: _te.Self) -> _te.Self:
        ...

    def mul(self, other: _te.Self) -> _te.Self:
        ...

    def rem(self, divisor: _te.Self) -> _te.Self:
        ...

    def rem_euclid(self, divisor: _te.Self) -> _te.Self:
        ...

    def sub(self, other: _te.Self) -> _te.Self:
        ...

    def to_be_bytes(self) -> bytes:
        ...

    def to_le_bytes(self) -> bytes:
        ...

    def to_ne_bytes(self) -> bytes:
        ...

    @_t.overload
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __and__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __and__(self, other: _t.Any) -> _t.Any:
        ...

    def __bool__(self) -> _t.NoReturn:
        ...

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __ge__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __init__(self, _value: int) -> None:
        ...

    def __invert__(self) -> _te.Self:
        ...

    def __int__(self) -> int:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool_:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __lshift__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __mod__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mod__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mul__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __rshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __rshift__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __sub__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __truediv__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __truediv__(self, other: _t.Any) -> _t.Any:
        ...


class _BaseSignedInteger(_BaseInteger):
    def abs(self) -> _te.Self:
        ...

    def checked_abs(self) -> _Option[_te.Self]:
        ...

    def checked_neg(self) -> _Option[_te.Self]:
        ...

    def is_negative(self) -> bool_:
        ...

    def is_positive(self) -> bool_:
        ...

    def neg(self) -> _te.Self:
        ...

    def __neg__(self) -> _te.Self:
        ...


class _BaseUnsignedInteger(_BaseInteger):
    ...


@_te.final
class i128(_BaseSignedInteger):
    pass


@_te.final
class i16(_BaseSignedInteger):
    pass


@_te.final
class i32(_BaseSignedInteger):
    pass


@_te.final
class i64(_BaseSignedInteger):
    pass


@_te.final
class i8(_BaseSignedInteger):
    pass


@_te.final
class isize(_BaseSignedInteger):
    pass


@_te.final
class str_:
    pass


@_te.final
class u128(_BaseUnsignedInteger):
    pass


@_te.final
class u16(_BaseUnsignedInteger):
    pass


@_te.final
class u32(_BaseUnsignedInteger):
    pass


@_te.final
class u64(_BaseUnsignedInteger):
    pass


@_te.final
class u8(_BaseUnsignedInteger):
    pass


@_te.final
class usize(_BaseUnsignedInteger):
    pass


_CastableFromBool = _t.TypeVar('_CastableFromBool', _BaseInteger, bool_)
_PrimitiveNumberT = _t.TypeVar('_PrimitiveNumberT', _BaseInteger, _BaseFloat)
