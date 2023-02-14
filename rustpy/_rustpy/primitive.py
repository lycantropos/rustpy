from ctypes import c_float

import typing_extensions as _te

from ._core import bool_ as _bool
from ._core.float import BaseFloat
from ._core.integer import (
    SIZE_BITS as _SIZE_BITS,
    BaseSignedInteger as _BaseSignedInteger,
    BaseUnsignedInteger as _BaseUnsignedInteger,
    signed_cls_to_max_value as _signed_cls_to_max_value,
    signed_cls_to_min_value as _signed_cls_to_min_value,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value,
    unsigned_cls_to_min_value as _unsigned_cls_to_min_value
)

bool_ = _bool.bool_


@_te.final
class f32(BaseFloat):
    def __init__(self, _value: float) -> None:
        self._value = c_float(_value).value


@_te.final
class f64(BaseFloat):
    pass


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


isize.BITS = u32(_SIZE_BITS)
isize.MAX = _signed_cls_to_max_value(isize)
isize.MIN = _signed_cls_to_min_value(isize)


@_te.final
class u8(_BaseUnsignedInteger):
    pass


u8.BITS = u32(8)
u8.MAX = _unsigned_cls_to_max_value(u8)
u8.MIN = _unsigned_cls_to_min_value(u8)


@_te.final
class u16(_BaseUnsignedInteger):
    pass


u16.BITS = u32(16)
u16.MAX = _unsigned_cls_to_max_value(u16)
u16.MIN = _unsigned_cls_to_min_value(u16)


@_te.final
class u64(_BaseUnsignedInteger):
    pass


u64.BITS = u32(64)
u64.MAX = _unsigned_cls_to_max_value(u64)
u64.MIN = _unsigned_cls_to_min_value(u64)


@_te.final
class u128(_BaseUnsignedInteger):
    pass


u128.BITS = u32(128)
u128.MAX = _unsigned_cls_to_max_value(u128)
u128.MIN = _unsigned_cls_to_min_value(u128)


@_te.final
class usize(_BaseUnsignedInteger):
    pass


usize.BITS = u32(_SIZE_BITS)
usize.MAX = _unsigned_cls_to_max_value(usize)
usize.MIN = _unsigned_cls_to_min_value(usize)
