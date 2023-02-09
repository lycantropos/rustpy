from typing import TypeVar

from rustpy import primitive

Primitive = TypeVar('Primitive', primitive.bool_, primitive.i128,
                    primitive.i16, primitive.i32, primitive.i64, primitive.i8,
                    primitive.isize, primitive.u128, primitive.u16,
                    primitive.u32, primitive.u64, primitive.u8,
                    primitive.usize)


def equivalence(first: bool, second: bool) -> bool:
    return first is second


def implication(antecedent: bool, consequent: bool) -> bool:
    return not antecedent or consequent
