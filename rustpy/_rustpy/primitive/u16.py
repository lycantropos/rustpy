import typing_extensions as _te

from ._core.integer import (
    BaseUnsignedInteger as _BaseUnsignedInteger,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value
)
from .u32 import u32 as _u32


@_te.final
class u16(_BaseUnsignedInteger):
    pass


u16.BITS = _u32(16)
u16.MAX = _unsigned_cls_to_max_value(u16)
u16.MIN = u16(0)
