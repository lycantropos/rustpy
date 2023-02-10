import typing_extensions as _te

from ._core.integer import (
    SIZE_BITS as _SIZE_BITS,
    BaseUnsignedInteger as _BaseUnsignedInteger,
    unsigned_cls_to_max_value as _unsigned_cls_to_max_value
)
from .u32 import u32 as _u32


@_te.final
class usize(_BaseUnsignedInteger):
    pass


usize.BITS = _u32(_SIZE_BITS)
usize.MAX = _unsigned_cls_to_max_value(usize)
usize.MIN = usize(0)
