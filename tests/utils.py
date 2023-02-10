from typing import TypeVar

from rustpy.primitive.bool_ import bool_
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

Primitive = TypeVar('Primitive', bool_, i128, i16, i32, i64, i8, isize, u128,
                    u16, u32, u64, u8, usize)


def equivalence(first: bool, second: bool) -> bool:
    return first is second


def implication(antecedent: bool, consequent: bool) -> bool:
    return not antecedent or consequent
