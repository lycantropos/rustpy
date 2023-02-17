from hypothesis import strategies as _st

from tests.strategies import (
    equatable_primitives_values as _equatable_primitives_values
)

finite_primitives = _st.one_of(_equatable_primitives_values)
finite_primitives_pairs = _st.one_of(
        [_st.tuples(values, values) for values in _equatable_primitives_values]
)
finite_primitives_triplets = _st.one_of(
        [_st.tuples(values, values, values)
         for values in _equatable_primitives_values]
)
