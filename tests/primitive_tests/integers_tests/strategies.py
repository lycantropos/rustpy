import typing as _t

from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy as _SearchStrategy

from rustpy import primitive as _primitive
from tests.utils import (Integer as _Integer,
                         rust_int_to_python_int as _rust_int_to_python_int)


def _to_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    return (_st.integers(_rust_int_to_python_int(cls.MIN),
                         _rust_int_to_python_int(cls.MAX))
            .map(cls))


def _to_non_zero_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    min_value = _rust_int_to_python_int(cls.MIN)
    return (((_st.nothing() if min_value == 0 else _st.integers(min_value, -1))
             | _st.integers(1, _rust_int_to_python_int(cls.MAX)))
            .map(cls))


def _to_unit_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    return _st.builds(cls, _st.just(1))


def _to_zero_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    return _st.builds(cls, _st.just(0))


signed_integer_types = (_primitive.i8, _primitive.i16, _primitive.i32,
                        _primitive.i64, _primitive.i128, _primitive.isize)
unsigned_integer_types = (_primitive.u8, _primitive.u16, _primitive.u32,
                          _primitive.u64, _primitive.u128, _primitive.usize)
integer_types = (*signed_integer_types, *unsigned_integer_types)

divisible_integers_pairs = _st.one_of(
        [_st.tuples(_to_integers(integer_type),
                    _to_non_zero_integers(integer_type))
         for integer_type in integer_types]
)
integers_with_zeros = _st.one_of([_st.tuples(_to_integers(integer_type),
                                             _to_zero_integers(integer_type))
                                  for integer_type in integer_types])
integers_with_ones = _st.one_of([_st.tuples(_to_integers(integer_type),
                                            _to_unit_integers(integer_type))
                                 for integer_type in integer_types])
signed_integer_values = tuple(_to_integers(integer_type)
                              for integer_type in signed_integer_types)
unsigned_integer_values = tuple(_to_integers(integer_type)
                                for integer_type in unsigned_integer_types)
integer_values = (*signed_integer_values, *unsigned_integer_values)
signed_integers = _st.one_of(signed_integer_values)
signed_divisible_integers_pairs = _st.one_of(
        [_st.tuples(_to_integers(integer_type),
                    _to_non_zero_integers(integer_type))
         for integer_type in signed_integer_types]
)
signed_integers_pairs = _st.one_of([_st.tuples(values, values)
                                    for values in signed_integer_values])
integers_pairs = _st.one_of([_st.tuples(values, values)
                             for values in integer_values])
