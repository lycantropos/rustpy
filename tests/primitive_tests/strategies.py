from typing import (Any,
                    Type)

from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy

from rustpy import primitive
from tests.utils import Integer

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


def to_non_zero_integers(cls: Type[Integer]) -> SearchStrategy[Integer]:
    min_value = rust_int_to_python_int(cls.MIN)
    return (((_st.nothing() if min_value == 0 else _st.integers(min_value, -1))
             | _st.integers(1, rust_int_to_python_int(cls.MAX)))
            .map(cls))


def to_zero_integers(cls: Type[Integer]) -> SearchStrategy[Integer]:
    return _st.builds(cls, _st.just(0))


def rust_int_to_python_int(value: Any) -> int:
    return int(str(value)[:-len(type(value).__qualname__)])


signed_integer_types = (primitive.i8, primitive.i16, primitive.i32,
                        primitive.i64, primitive.i128, primitive.isize)
unsigned_integer_types = (primitive.u8, primitive.u16, primitive.u32,
                          primitive.u64, primitive.u128, primitive.usize)
integer_types = (*signed_integer_types, *unsigned_integer_types)
i8s = to_integers(primitive.i8)
i16s = to_integers(primitive.i16)
i32s = to_integers(primitive.i32)
i64s = to_integers(primitive.i64)
i128s = to_integers(primitive.i128)
isizes = to_integers(primitive.isize)

u8s = to_integers(primitive.u8)
u16s = to_integers(primitive.u16)
u32s = to_integers(primitive.u32)
u64s = to_integers(primitive.u64)
u128s = to_integers(primitive.u128)
usizes = to_integers(primitive.usize)

finite_floats_values = finite_f32s, finite_f64s
signed_integer_values = i128s, i16s, i32s, i64s, i8s, isizes
unsigned_integer_values = u128s, u16s, u32s, u64s, u8s, usizes
integer_values = (*signed_integer_values, *unsigned_integer_values)
finite_primitives_values = (bools, *integer_values, *finite_floats_values)
integers = _st.one_of(integer_values)
integers_pairs = _st.one_of([_st.tuples(values, values)
                             for values in integer_values])
divisible_integers_pairs = _st.one_of(
        [_st.tuples(to_integers(integer_type),
                    to_non_zero_integers(integer_type))
         for integer_type in integer_types]
)
integers_with_zeros = _st.one_of([_st.tuples(to_integers(integer_type),
                                             to_zero_integers(integer_type))
                                  for integer_type in integer_types])
integers_triplets = _st.one_of([_st.tuples(values, values, values)
                                for values in integer_values])
finite_primitives = _st.one_of(finite_primitives_values)
finite_primitives_pairs = _st.one_of([_st.tuples(values, values)
                                      for values in finite_primitives_values])
finite_primitives_triplets = _st.one_of(
        [_st.tuples(values, values, values)
         for values in finite_primitives_values]
)
