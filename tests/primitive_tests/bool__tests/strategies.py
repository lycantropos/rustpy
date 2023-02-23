from hypothesis import strategies as _st

from rustpy import primitive as _primitive
from tests.utils import (to_unit_integers as _to_unit_integers,
                         to_zero_integers as _to_zero_integers)

_integer_types = [
    _primitive.i8, _primitive.i16, _primitive.i32, _primitive.i64,
    _primitive.i128, _primitive.isize, _primitive.u8, _primitive.u16,
    _primitive.u32, _primitive.u64, _primitive.u128, _primitive.usize
]
integer_types = _st.sampled_from(_integer_types)
bool_types = _st.just(_primitive.bool_)
bools = _st.booleans().map(_primitive.bool_)
bool_types_with_values = _st.tuples(bool_types, bools)
convertible_from_bool_types = bool_types | integer_types
integer_types_with_zeros_and_ones = _st.one_of([
    _st.tuples(_st.just(integer_type), _to_zero_integers(integer_type),
               _to_unit_integers(integer_type))
    for integer_type in _integer_types
])
