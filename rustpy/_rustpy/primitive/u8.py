import typing_extensions as _te

from ._core.integer import (
    BaseUnsignedInteger as _BaseUnsignedInteger,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value
)
from .u32 import u32 as _u32


@_te.final
class u8(_BaseUnsignedInteger):
    pass


u8.BITS = _u32(8)
u8.MAX = _unsigned_cls_to_max_value(u8)
u8.MIN = u8(0)
