from hypothesis import strategies as _st

from rustpy import primitive as _primitive
from rustpy.option import (None_ as _None,
                           Some as _Some)
from rustpy.result import (Err as _Err,
                           Ok as _Ok)
from tests.utils import (to_homogeneous_tuples as _to_homogeneous_tuples,
                         to_integers as _to_integers)

MAX_RECURSION_DEPTH = 3
hashable_equatable_values = _st.recursive(
        _st.none() | _st.sampled_from([Ellipsis, NotImplemented])
        | _st.booleans() | _st.integers() | _st.fractions()
        | _st.floats(allow_nan=False) | _st.complex_numbers(allow_nan=False)
        | _st.binary() | _st.text() | _st.dates() | _st.datetimes(),
        lambda values: _st.frozensets(values) | _to_homogeneous_tuples(values)
)
_bools = _st.builds(_primitive.bool_, _st.booleans())
_equatable_f32s = _st.builds(_primitive.f32, _st.floats(allow_nan=False,
                                                        allow_infinity=True,
                                                        width=32))
_equatable_f64s = _st.builds(_primitive.f64, _st.floats(allow_nan=False,
                                                        allow_infinity=True,
                                                        width=64))
_losslessly_representable_f32s = _st.builds(_primitive.f32,
                                            _st.floats(allow_nan=False,
                                                       allow_infinity=False,
                                                       width=32))
_losslessly_representable_f64s = _st.builds(_primitive.f64,
                                            _st.floats(allow_nan=False,
                                                       allow_infinity=False,
                                                       width=64))
signed_integer_types = (_primitive.i8, _primitive.i16, _primitive.i32,
                        _primitive.i64, _primitive.i128, _primitive.isize)
unsigned_integer_types = (_primitive.u8, _primitive.u16, _primitive.u32,
                          _primitive.u64, _primitive.u128, _primitive.usize)
_comparable_floats_values = _equatable_f32s, _equatable_f64s
_losslessly_representable_floats_values = (_losslessly_representable_f32s,
                                           _losslessly_representable_f64s)
_signed_integer_values = tuple(_to_integers(integer_type)
                               for integer_type in signed_integer_types)
_unsigned_integer_values = tuple(_to_integers(integer_type)
                                 for integer_type in unsigned_integer_types)
_integer_values = (*_signed_integer_values, *_unsigned_integer_values)
comparable_primitives_values = (_bools, *_integer_values,
                                *_comparable_floats_values)
losslessly_representable_primitives_values = (
    _bools, *_integer_values, *_losslessly_representable_floats_values
)
nones = _st.builds(_None)
equatable_values = _st.recursive(
        (hashable_equatable_values | _st.sets(hashable_equatable_values)
         | _st.one_of(comparable_primitives_values) | nones),
        lambda values:
        (_st.lists(values) | _to_homogeneous_tuples(values)
         | _st.dictionaries(hashable_equatable_values, values)
         | values.map(_Some) | values.map(_Err) | values.map(_Ok)),
        max_leaves=MAX_RECURSION_DEPTH
)
_comparable_homogeneous_values_categories = _st.recursive(
        _st.sampled_from([_st.booleans() | _st.integers() | _st.fractions()
                          | _st.floats(allow_nan=False),
                          _st.binary(), _st.text(), _st.dates(),
                          _st.datetimes(),
                          *comparable_primitives_values]),
        lambda base: base.map(_st.lists) | base.map(_to_homogeneous_tuples),
        max_leaves=MAX_RECURSION_DEPTH
)
comparable_values_categories = _st.recursive(
        _comparable_homogeneous_values_categories,
        lambda base:
        (_st.lists(base).map(lambda values: _st.tuples(*values))
         | base.map(lambda values: _st.builds(_None) | values.map(_Some))
         | base.map(lambda values: values.map(_Err) | values.map(_Ok))),
        max_leaves=MAX_RECURSION_DEPTH
)
hashable_losslessly_representable_values = _st.recursive(
        _st.none() | _st.sampled_from([Ellipsis, NotImplemented])
        | _st.booleans() | _st.integers()
        | _st.floats(allow_infinity=False,
                     allow_nan=False)
        | _st.complex_numbers(allow_infinity=False,
                              allow_nan=False)
        | _st.binary() | _st.text(),
        lambda values: _st.frozensets(values) | _to_homogeneous_tuples(values),
        max_leaves=MAX_RECURSION_DEPTH
)
losslessly_representable_values = _st.recursive(
        hashable_losslessly_representable_values
        | _st.one_of(losslessly_representable_primitives_values) | nones,
        lambda values:
        (_st.lists(values) | _to_homogeneous_tuples(values)
         | _st.dictionaries(hashable_losslessly_representable_values, values)
         | values.map(_Some) | values.map(_Err) | values.map(_Ok)),
        max_leaves=MAX_RECURSION_DEPTH
)
