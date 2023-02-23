from __future__ import annotations

import math as _math
import struct as _struct
import typing as _t
from ctypes import c_float

import typing_extensions as _te

from ._core.bool_ import bool_ as _bool
from ._core.float import BaseFloat as _BaseFloat
from ._core.integer import (
    SIZE_BITS as _SIZE_BITS,
    BaseSignedInteger as _BaseSignedInteger,
    BaseUnsignedInteger as _BaseUnsignedInteger,
    signed_cls_to_max_value as _signed_cls_to_max_value,
    signed_cls_to_min_value as _signed_cls_to_min_value,
    u32_to_int as _u32_to_int,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value,
    unsigned_cls_to_min_value as _unsigned_cls_to_min_value
)

bool_ = _bool


class _CastableBaseSignedInteger(_BaseSignedInteger):
    def as_(self, cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
        if issubclass(cls, (_CastableBaseSignedInteger,
                            _CastableBaseUnsignedInteger)):
            return cls.from_le_bytes(
                    self.to_le_bytes()[:_u32_to_int(cls.BITS) // 8]
                    if self.BITS > cls.BITS
                    else self._value.to_bytes(_u32_to_int(cls.BITS) // 8,
                                              'little',
                                              signed=True)
            )
        elif issubclass(cls, _BaseFloat):
            return cls(float(self._value))
        else:
            raise TypeError(cls)


class _CastableBaseUnsignedInteger(_BaseUnsignedInteger):
    def as_(self, cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
        if issubclass(cls, (_CastableBaseSignedInteger,
                            _CastableBaseUnsignedInteger)):
            return cls.from_le_bytes(
                    self.to_le_bytes()[:_u32_to_int(cls.BITS) // 8]
                    if self.BITS > cls.BITS
                    else self._value.to_bytes(_u32_to_int(cls.BITS) // 8,
                                              'little')
            )
        elif issubclass(cls, _BaseFloat):
            return cls(float(self._value))
        else:
            raise TypeError(cls)


@_te.final
class u32(_CastableBaseUnsignedInteger):
    pass


u32.BITS = u32(32)
u32.MAX = _unsigned_cls_to_max_value(u32)
u32.MIN = u32(0)


@_te.final
class i8(_CastableBaseSignedInteger):
    pass


i8.BITS = u32(8)
i8.MAX = _signed_cls_to_max_value(i8)
i8.MIN = _signed_cls_to_min_value(i8)


@_te.final
class i16(_CastableBaseSignedInteger):
    pass


i16.BITS = u32(16)
i16.MAX = _signed_cls_to_max_value(i16)
i16.MIN = _signed_cls_to_min_value(i16)


@_te.final
class i32(_CastableBaseSignedInteger):
    pass


i32.BITS = u32(32)
i32.MAX = _signed_cls_to_max_value(i32)
i32.MIN = _signed_cls_to_min_value(i32)


@_te.final
class i64(_CastableBaseSignedInteger):
    pass


i64.BITS = u32(64)
i64.MAX = _signed_cls_to_max_value(i64)
i64.MIN = _signed_cls_to_min_value(i64)


@_te.final
class i128(_CastableBaseSignedInteger):
    pass


i128.BITS = u32(128)
i128.MAX = _signed_cls_to_max_value(i128)
i128.MIN = _signed_cls_to_min_value(i128)


@_te.final
class isize(_CastableBaseSignedInteger):
    pass


isize.BITS = u32(_SIZE_BITS)
isize.MAX = _signed_cls_to_max_value(isize)
isize.MIN = _signed_cls_to_min_value(isize)


@_te.final
class u8(_CastableBaseUnsignedInteger):
    pass


u8.BITS = u32(8)
u8.MAX = _unsigned_cls_to_max_value(u8)
u8.MIN = _unsigned_cls_to_min_value(u8)


@_te.final
class u16(_CastableBaseUnsignedInteger):
    pass


u16.BITS = u32(16)
u16.MAX = _unsigned_cls_to_max_value(u16)
u16.MIN = _unsigned_cls_to_min_value(u16)


@_te.final
class u64(_CastableBaseUnsignedInteger):
    pass


u64.BITS = u32(64)
u64.MAX = _unsigned_cls_to_max_value(u64)
u64.MIN = _unsigned_cls_to_min_value(u64)


@_te.final
class u128(_CastableBaseUnsignedInteger):
    pass


u128.BITS = u32(128)
u128.MAX = _unsigned_cls_to_max_value(u128)
u128.MIN = _unsigned_cls_to_min_value(u128)


@_te.final
class usize(_CastableBaseUnsignedInteger):
    pass


usize.BITS = u32(_SIZE_BITS)
usize.MAX = _unsigned_cls_to_max_value(usize)
usize.MIN = _unsigned_cls_to_min_value(usize)


@_te.final
class f32(_BaseFloat):
    @classmethod
    def from_be_bytes(cls, _bytes: bytes) -> _te.Self:
        try:
            value, = _struct.unpack('>f', _bytes)
        except _struct.error:
            raise TypeError(f'Invalid number of bytes, got {len(_bytes)}.')
        else:
            return cls(value)

    @classmethod
    def from_le_bytes(cls, _bytes: bytes) -> _te.Self:
        try:
            value, = _struct.unpack('<f', _bytes)
        except _struct.error:
            raise TypeError(f'Invalid number of bytes, got {len(_bytes)}.')
        else:
            return cls(value)

    @classmethod
    def from_ne_bytes(cls, _bytes: bytes) -> _te.Self:
        try:
            value, = _struct.unpack('=f', _bytes)
        except _struct.error:
            raise TypeError(f'Invalid number of bytes, got {len(_bytes)}.')
        else:
            return cls(value)

    def as_(self, cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
        return _cast_float_as(self._value, cls)

    def to_be_bytes(self) -> bytes:
        return _struct.pack('>f', self._value)

    def to_le_bytes(self) -> bytes:
        return _struct.pack('<f', self._value)

    def to_ne_bytes(self) -> bytes:
        return _struct.pack('=f', self._value)

    def __init__(self, _value: float) -> None:
        self._value = c_float(_value).value


f32.DIGITS = u32(6)
f32.EPSILON = f32(1.1920929e-7)
f32.INFINITY = f32(_math.inf)
f32.MANTISSA_DIGITS = u32(24)
f32.MAX = f32(3.40282347e+38)
f32.MAX_10_EXP = i32(38)
f32.MAX_EXP = i32(128)
f32.MIN = f32(-3.40282347e+38)
f32.MIN_10_EXP = i32(-37)
f32.MIN_EXP = i32(-125)
f32.MIN_POSITIVE = f32(1.17549435e-38)
f32.NAN = f32(_math.nan)
f32.NEG_INFINITY = f32(-_math.inf)
f32.RADIX = u32(2)


@_te.final
class f64(_BaseFloat):
    @classmethod
    def from_be_bytes(cls, _bytes: bytes) -> _te.Self:
        try:
            value, = _struct.unpack('>d', _bytes)
            return cls(value)
        except _struct.error:
            raise TypeError(f'Invalid number of bytes, got {len(_bytes)}.')

    @classmethod
    def from_le_bytes(cls, _bytes: bytes) -> _te.Self:
        try:
            value, = _struct.unpack('<d', _bytes)
            return cls(value)
        except _struct.error:
            raise TypeError(f'Invalid number of bytes, got {len(_bytes)}.')

    @classmethod
    def from_ne_bytes(cls, _bytes: bytes) -> _te.Self:
        try:
            value, = _struct.unpack('=d', _bytes)
            return cls(value)
        except _struct.error:
            raise TypeError(f'Invalid number of bytes, got {len(_bytes)}.')

    def as_(self, cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
        return _cast_float_as(self._value, cls)

    def to_be_bytes(self) -> bytes:
        return _struct.pack('>d', self._value)

    def to_le_bytes(self) -> bytes:
        return _struct.pack('<d', self._value)

    def to_ne_bytes(self) -> bytes:
        return _struct.pack('=d', self._value)


f64.DIGITS = u32(15)
f64.EPSILON = f64(2.2204460492503131e-16)
f64.INFINITY = f64(_math.inf)
f64.MANTISSA_DIGITS = u32(53)
f64.MAX = f64(1.7976931348623157e+308)
f64.MAX_10_EXP = i32(308)
f64.MAX_EXP = i32(1_024)
f64.MIN = f64(-1.7976931348623157e+308)
f64.MIN_10_EXP = i32(-307)
f64.MIN_EXP = i32(-1_021)
f64.MIN_POSITIVE = f64(2.2250738585072014e-308)
f64.NAN = f64(_math.nan)
f64.NEG_INFINITY = f64(-_math.inf)
f64.RADIX = u32(2)

_PrimitiveNumberT = _t.TypeVar(
        '_PrimitiveNumberT', _BaseFloat, _CastableBaseSignedInteger,
        _CastableBaseUnsignedInteger
)


def _cast_float_as(value: float,
                   cls: _t.Type[_PrimitiveNumberT]) -> _PrimitiveNumberT:
    if issubclass(cls, _BaseFloat):
        return cls(value)
    elif issubclass(cls, (_CastableBaseSignedInteger,
                          _CastableBaseUnsignedInteger)):
        try:
            return cls(int(value))
        except OverflowError:
            return cls.MIN if value < 0 else cls.MAX
        except ValueError:
            assert _math.isnan(value), value
            return cls(0)
    else:
        raise TypeError(cls)
