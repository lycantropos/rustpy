from typing import (Any,
                    Type)

from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy

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

bools = _st.builds(bool_, _st.booleans())

finite_f32s = _st.builds(f32, _st.floats(allow_nan=False,
                                         allow_infinity=False,
                                         width=32))
finite_f64s = _st.builds(f64, _st.floats(allow_nan=False,
                                         allow_infinity=False,
                                         width=64))


def to_integers(cls: Type[Any]) -> SearchStrategy[Any]:
    return (_st.integers(rust_int_to_python_int(cls.MIN),
                         rust_int_to_python_int(cls.MAX))
            .map(cls))


def rust_int_to_python_int(value: Any) -> int:
    return int(str(value)[:-len(type(value).__qualname__)])


i8s = to_integers(i8)
i16s = to_integers(i16)
i32s = to_integers(i32)
i64s = to_integers(i64)
i128s = to_integers(i128)
isizes = to_integers(isize)

u8s = to_integers(u8)
u16s = to_integers(u16)
u32s = to_integers(u32)
u64s = to_integers(u64)
u128s = to_integers(u128)
usizes = to_integers(usize)

finite_floats_values = finite_f32s, finite_f64s
signed_integers_values = i128s, i16s, i32s, i64s, i8s, isizes
unsigned_integers_values = u128s, u16s, u32s, u64s, u8s, usizes
integers_values = (*signed_integers_values, *unsigned_integers_values)
finite_primitives_values = (bools, *integers_values, *finite_floats_values)
finite_primitives = bools | _st.one_of(integers_values)
finite_primitives_pairs = _st.one_of([_st.tuples(values, values)
                                      for values in finite_primitives_values])
finite_primitives_triplets = _st.one_of(
        [_st.tuples(values, values, values)
         for values in finite_primitives_values]
)
integers_pairs = _st.one_of([_st.tuples(values, values)
                             for values in integers_values])
