from typing import Type

from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy

from rustpy import primitive
from tests.utils import (Integer,
                         rust_int_to_python_int)

bools = _st.builds(primitive.bool_, _st.booleans())

finite_f32s = _st.builds(primitive.f32, _st.floats(allow_nan=False,
                                                   allow_infinity=False,
                                                   width=32))
finite_f64s = _st.builds(primitive.f64, _st.floats(allow_nan=False,
                                                   allow_infinity=False,
                                                   width=64))


def to_integers(cls: Type[Integer]) -> SearchStrategy[Integer]:
    return (_st.integers(rust_int_to_python_int(cls.MIN),
                         rust_int_to_python_int(cls.MAX))
            .map(cls))


signed_integer_types = (primitive.i8, primitive.i16, primitive.i32,
                        primitive.i64, primitive.i128, primitive.isize)
unsigned_integer_types = (primitive.u8, primitive.u16, primitive.u32,
                          primitive.u64, primitive.u128, primitive.usize)
integer_types = (*signed_integer_types, *unsigned_integer_types)

finite_floats_values = finite_f32s, finite_f64s
signed_integer_values = tuple(to_integers(integer_type)
                              for integer_type in signed_integer_types)
unsigned_integer_values = tuple(to_integers(integer_type)
                                for integer_type in unsigned_integer_types)
integer_values = (*signed_integer_values, *unsigned_integer_values)
finite_primitives_values = (bools, *integer_values, *finite_floats_values)
finite_primitives = _st.one_of(finite_primitives_values)
finite_primitives_pairs = _st.one_of([_st.tuples(values, values)
                                      for values in finite_primitives_values])
finite_primitives_triplets = _st.one_of(
        [_st.tuples(values, values, values)
         for values in finite_primitives_values]
)
