import typing_extensions as _te

from ._core.integer import (
    SIZE_BITS as _SIZE_BITS,
    BaseSignedInteger as _BaseSignedInteger,
    signed_cls_to_max_value as _signed_cls_to_max_value,
    signed_cls_to_min_value as _signed_cls_to_min_value
)
from .u32 import u32 as _u32


@_te.final
class isize(_BaseSignedInteger):
    pass


isize.BITS = _u32(_SIZE_BITS)
isize.MAX = _signed_cls_to_max_value(isize)
isize.MIN = _signed_cls_to_min_value(isize)
