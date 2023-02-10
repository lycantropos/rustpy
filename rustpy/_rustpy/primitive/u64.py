import typing_extensions as _te

from ._core.integer import (
    BaseUnsignedInteger as _BaseUnsignedInteger,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value
)
from .u32 import u32 as _u32


@_te.final
class u64(_BaseUnsignedInteger):
    pass


u64.BITS = _u32(64)
u64.MAX = _unsigned_cls_to_max_value(u64)
u64.MIN = u64(0)
