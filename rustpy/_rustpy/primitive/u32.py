import typing_extensions as _te

from ._core.integer import (
    BaseUnsignedInteger as _BaseUnsignedInteger,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value
)


@_te.final
class u32(_BaseUnsignedInteger):
    pass


u32.BITS = u32(32)
u32.MAX = _unsigned_cls_to_max_value(u32)
u32.MIN = u32(0)
