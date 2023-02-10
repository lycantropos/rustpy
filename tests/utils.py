import typing as _t

from rustpy.primitive.bool_ import bool_
from rustpy.primitive.f32 import f32
from rustpy.primitive.f64 import f64
from rustpy.primitive.i128 import i128
from rustpy.primitive.i16 import i16
from rustpy.primitive.i32 import i32
from rustpy.primitive.i64 import i64
from rustpy.primitive.i8 import i8
from rustpy.primitive.isize import isize
from rustpy.primitive.u128 import u128
from rustpy.primitive.u16 import u16
from rustpy.primitive.u32 import u32
from rustpy.primitive.u64 import u64
from rustpy.primitive.u8 import u8
from rustpy.primitive.usize import usize

Primitive = _t.TypeVar('Primitive', bool_, f32, f64, i128, i16, i32, i64, i8,
                       isize, u128, u16, u32, u64, u8, usize)

_AnyBool = _t.Union[bool, bool_]


def equivalence(first: _AnyBool, second: _AnyBool) -> bool:
    return bool(first) is bool(second)


def implication(antecedent: _AnyBool, consequent: _AnyBool) -> bool:
    return not antecedent or bool(consequent)
