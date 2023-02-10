import typing_extensions as _te

from ._core.integer import (
    BaseSignedInteger as _BaseSignedInteger,
    signed_cls_to_max_value as _signed_cls_to_max_value,
    signed_cls_to_min_value as _signed_cls_to_min_value
)
from .u32 import u32 as _u32


@_te.final
class i16(_BaseSignedInteger):
    pass


i16.BITS = _u32(16)
i16.MAX = _signed_cls_to_max_value(i16)
i16.MIN = _signed_cls_to_min_value(i16)
