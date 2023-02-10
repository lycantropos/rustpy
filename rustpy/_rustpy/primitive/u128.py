import typing_extensions as _te

from ._core.integer import (
    BaseUnsignedInteger as _BaseUnsignedInteger,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value
)
from .u32 import u32 as _u32


@_te.final
class u128(_BaseUnsignedInteger):
    pass


u128.BITS = _u32(128)
u128.MAX = _unsigned_cls_to_max_value(u128)
u128.MIN = u128(0)
