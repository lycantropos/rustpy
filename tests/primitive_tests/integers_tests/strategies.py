import typing as _t

from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy as _SearchStrategy

from rustpy import primitive as _primitive
from tests.utils import (Integer as _Integer,
                         rust_int_to_python_int as _rust_int_to_python_int,
                         to_integers as _to_integers)


def _to_non_zero_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    min_value = _rust_int_to_python_int(cls.MIN)
    return (((_st.nothing() if min_value == 0 else _st.integers(min_value, -1))
             | _st.integers(1, _rust_int_to_python_int(cls.MAX)))
            .map(cls))


def _to_unit_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    return _st.builds(cls, _st.just(1))


def _to_zero_integers(cls: _t.Type[_Integer]) -> _SearchStrategy[_Integer]:
    return _st.builds(cls, _st.just(0))


_float_types = _primitive.f32, _primitive.f64
signed_integer_types = (_primitive.i8, _primitive.i16, _primitive.i32,
                        _primitive.i64, _primitive.i128, _primitive.isize)
_unsigned_integer_types = (_primitive.u8, _primitive.u16, _primitive.u32,
                           _primitive.u64, _primitive.u128, _primitive.usize)
_integer_types = (*signed_integer_types, *_unsigned_integer_types)
float_types = _st.sampled_from(_float_types)
integer_types = _st.sampled_from(_integer_types)
numeric_types = _st.sampled_from([*_integer_types, *_float_types])

divisible_integers_pairs = _st.one_of(
        [_st.tuples(_to_integers(integer_type),
                    _to_non_zero_integers(integer_type))
         for integer_type in _integer_types]
)
integers_with_zeros = _st.one_of([_st.tuples(_to_integers(integer_type),
                                             _to_zero_integers(integer_type))
                                  for integer_type in _integer_types])
integers_with_ones = _st.one_of([_st.tuples(_to_integers(integer_type),
                                            _to_unit_integers(integer_type))
                                 for integer_type in _integer_types])
_signed_integer_values = tuple(_to_integers(integer_type)
                               for integer_type in signed_integer_types)
_unsigned_integer_values = tuple(_to_integers(integer_type)
                                 for integer_type in _unsigned_integer_types)
_integer_values = (*_signed_integer_values, *_unsigned_integer_values)
integer_types_with_values = _st.one_of([_st.tuples(_st.just(integer_type),
                                                   _to_integers(integer_type))
                                        for integer_type in _integer_types])
integers = _st.one_of(_integer_values)
zero_integers = _st.one_of([_to_zero_integers(integer_type)
                            for integer_type in _integer_types])
u32s = _to_integers(_primitive.u32)
u32_zeros = _to_zero_integers(_primitive.u32)
integers_pairs = _st.one_of([_st.tuples(values, values)
                             for values in _integer_values])
integers_triplets = _st.one_of([_st.tuples(values, values, values)
                                for values in _integer_values])
signed_integers = _st.one_of(_signed_integer_values)
signed_integers_pairs = _st.one_of([_st.tuples(values, values)
                                    for values in _signed_integer_values])
divisible_signed_integers_pairs = _st.one_of(
        [_st.tuples(_to_integers(integer_type),
                    _to_non_zero_integers(integer_type))
         for integer_type in signed_integer_types]
)
signed_integers_with_zeros = _st.one_of(
        [_st.tuples(_to_integers(integer_type),
                    _to_zero_integers(integer_type))
         for integer_type in signed_integer_types]
)
