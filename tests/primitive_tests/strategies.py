from hypothesis import strategies as _st

from tests.strategies import (
    comparable_primitives_values as _comparable_primitives_values,
    losslessly_representable_primitives_values
    as _losslessly_representable_primitives_values
)

comparable_primitives = _st.one_of(_comparable_primitives_values)
comparable_primitives_pairs = _st.one_of(
        [_st.tuples(values, values)
         for values in _comparable_primitives_values]
)
comparable_primitives_triplets = _st.one_of(
        [_st.tuples(values, values, values)
         for values in _comparable_primitives_values]
)
losslessly_representable_primitives = _st.one_of(
        _losslessly_representable_primitives_values
)
