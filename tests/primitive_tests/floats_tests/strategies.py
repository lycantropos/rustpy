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
    return _st.builds(cls, _st.just(1.0))


def _to_zero_floats(cls: _t.Type[_Float]) -> _SearchStrategy[_Float]:
    return _st.builds(cls, _st.just(0.0))


float_types = _primitive.f32, _primitive.f64

finite_floats_values = tuple(_to_floats(float_type,
                                        finite=True)
                             for float_type in float_types)
floats_values = tuple(_to_floats(float_type,
                                 finite=False)
                      for float_type in float_types)
floats = _st.one_of(floats_values)
finite_floats = _st.one_of(finite_floats_values)
finite_floats_pairs = _st.one_of([_st.tuples(values, values)
                                  for values in finite_floats_values])
finite_floats_with_ones = _st.one_of([_st.tuples(_to_floats(float_type,
                                                            finite=True),
                                                 _to_unit_floats(float_type))
                                      for float_type in float_types])
finite_floats_with_zeros = _st.one_of(
        [_st.tuples(_to_floats(float_type,
                               finite=True),
                    _to_zero_floats(float_type))
         for float_type in float_types]
)
