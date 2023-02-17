from hypothesis import strategies as _st

from rustpy import primitive as _primitive
from rustpy.option import (None_ as _None,
                           Some as _Some)
from rustpy.result import (Err as _Err,
                           Ok as _Ok)
from tests.utils import to_integers as _to_integers

MAX_RECURSION_DEPTH = 3
hashable_equatable_values = _st.recursive(
        _st.none() | _st.sampled_from([Ellipsis, NotImplemented])
        | _st.booleans() | _st.integers() | _st.fractions()
        | _st.floats(allow_nan=False) | _st.complex_numbers(allow_nan=False)
        | _st.binary() | _st.text() | _st.dates() | _st.datetimes(),
        lambda values: _st.frozensets(values) | _st.lists(values).map(tuple)
)
_bools = _st.builds(_primitive.bool_, _st.booleans())
_equatable_f32s = _st.builds(_primitive.f32, _st.floats(allow_nan=False,
                                                        allow_infinity=True,
                                                        width=32))
_equatable_f64s = _st.builds(_primitive.f64, _st.floats(allow_nan=False,
                                                        allow_infinity=True,
                                                        width=64))
_lossless_representable_f32s = _st.builds(_primitive.f32,
                                          _st.floats(allow_nan=False,
                                                     allow_infinity=False,
                                                     width=32))
_lossless_representable_f64s = _st.builds(_primitive.f64,
                                          _st.floats(allow_nan=False,
                                                     allow_infinity=False,
                                                     width=64))
signed_integer_types = (_primitive.i8, _primitive.i16, _primitive.i32,
                        _primitive.i64, _primitive.i128, _primitive.isize)
unsigned_integer_types = (_primitive.u8, _primitive.u16, _primitive.u32,
                          _primitive.u64, _primitive.u128, _primitive.usize)
_equatable_floats_values = _equatable_f32s, _equatable_f64s
_lossless_representable_floats_values = (_lossless_representable_f32s,
                                         _lossless_representable_f64s)
_signed_integer_values = tuple(_to_integers(integer_type)
                               for integer_type in signed_integer_types)
_unsigned_integer_values = tuple(_to_integers(integer_type)
                                 for integer_type in unsigned_integer_types)
_integer_values = (*_signed_integer_values, *_unsigned_integer_values)
equatable_primitives_values = (_bools, *_integer_values,
                               *_equatable_floats_values)
lossless_representable_primitives_values = (
    _bools, *_integer_values, *_lossless_representable_floats_values
)
nones = _st.builds(_None)
equatable_values = _st.recursive(
        (hashable_equatable_values | _st.sets(hashable_equatable_values)
         | _st.one_of(equatable_primitives_values) | nones),
        lambda values:
        (_st.lists(values) | _st.lists(values).map(tuple)
         | _st.dictionaries(hashable_equatable_values, values)
         | values.map(_Some) | values.map(_Err) | values.map(_Ok)),
        max_leaves=MAX_RECURSION_DEPTH
)
hashable_lossless_representable_values = _st.recursive(
        _st.none() | _st.sampled_from([Ellipsis, NotImplemented])
        | _st.booleans() | _st.integers()
        | _st.floats(allow_infinity=False,
                     allow_nan=False)
        | _st.complex_numbers(allow_infinity=False,
                              allow_nan=False)
        | _st.binary() | _st.text(),
        lambda values: _st.frozensets(values) | _st.lists(values).map(tuple),
        max_leaves=MAX_RECURSION_DEPTH
)
lossless_representable_values = _st.recursive(
        hashable_lossless_representable_values
        | _st.one_of(lossless_representable_primitives_values) | nones,
        lambda values:
        (_st.lists(values) | _st.lists(values).map(tuple)
         | _st.dictionaries(hashable_lossless_representable_values, values)
         | values.map(_Some) | values.map(_Err) | values.map(_Ok)),
        max_leaves=MAX_RECURSION_DEPTH
)
