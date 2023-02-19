import typing as _t

from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy as _SearchStrategy

from rustpy import primitive as _primitive
from tests.utils import Float as _Float


def _to_floats(cls: _t.Type[_Float],
               *,
               finite: bool) -> _SearchStrategy[_Float]:
    assert cls is _primitive.f32 or cls is _primitive.f64
    return _st.floats(allow_nan=not finite,
                      allow_infinity=not finite,
                      width=32 if cls is _primitive.f32 else 64).map(cls)


def _to_unit_floats(cls: _t.Type[_Float]) -> _SearchStrategy[_Float]:
    return _st.just(1.0).map(cls)


def _to_zero_floats(cls: _t.Type[_Float]) -> _SearchStrategy[_Float]:
    return _st.just(0.0).map(cls)


_float_types = _primitive.f32, _primitive.f64
float_types = _st.sampled_from(_float_types)
_integer_types = [
    _primitive.i8, _primitive.i16, _primitive.i32, _primitive.i64,
    _primitive.i128, _primitive.isize, _primitive.u8, _primitive.u16,
    _primitive.u32, _primitive.u64, _primitive.u128, _primitive.usize
]
numeric_types = _st.sampled_from([*_integer_types, *_float_types])
integer_types_with_zeros = _st.one_of([
    _st.tuples(_st.just(integer_type), _st.just(0).map(integer_type))
    for integer_type in _integer_types
])
float_types_with_zeros = _st.one_of([
    _st.tuples(_st.just(float_type), _to_zero_floats(float_type))
    for float_type in _float_types
])
numeric_types_with_zeros = integer_types_with_zeros | float_types_with_zeros

_finite_floats_values = tuple(_to_floats(float_type,
                                         finite=True)
                              for float_type in _float_types)
_floats_values = tuple(_to_floats(float_type,
                                  finite=False)
                       for float_type in _float_types)
float_types_with_finite_values = _st.one_of(
        [_st.tuples(_st.just(float_type), _to_floats(float_type,
                                                     finite=True))
         for float_type in _float_types]
)
float_types_with_values = _st.one_of([_st.tuples(_st.just(float_type),
                                                 _to_floats(float_type,
                                                            finite=False))
                                      for float_type in _float_types])
floats = _st.one_of(_floats_values)
finite_floats = _st.one_of(_finite_floats_values)
finite_floats_pairs = _st.one_of([_st.tuples(values, values)
                                  for values in _finite_floats_values])
finite_floats_with_ones = _st.one_of([_st.tuples(_to_floats(float_type,
                                                            finite=True),
                                                 _to_unit_floats(float_type))
                                      for float_type in _float_types])
finite_floats_with_zeros = _st.one_of([_st.tuples(_to_floats(float_type,
                                                             finite=True),
                                                  _to_zero_floats(float_type))
                                       for float_type in _float_types])
floats_with_zeros = _st.one_of([_st.tuples(_to_floats(float_type,
                                                      finite=False),
                                           _to_zero_floats(float_type))
                                for float_type in _float_types])
