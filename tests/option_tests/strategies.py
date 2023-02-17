from functools import partial

from hypothesis import strategies as _st

from rustpy.option import (None_ as _None,
                           Some as _Some)
from tests.strategies import (MAX_RECURSION_DEPTH,
                              equatable_values,
                              lossless_representable_values)

comparable_values_categories_tuple = (
    _st.booleans() | _st.integers() | _st.fractions()
    | _st.floats(allow_nan=False),
    _st.binary(),
    _st.text(),
    _st.dates(),
    _st.datetimes()
)
comparable_values = _st.recursive(
        _st.one_of(comparable_values_categories_tuple),
        lambda values: _st.lists(values) | _st.lists(values).map(tuple),
        max_leaves=MAX_RECURSION_DEPTH
)
_comparable_values_categories = _st.recursive(
        _st.sampled_from(comparable_values_categories_tuple),
        lambda category:
        (category.map(_st.lists)
         | category.map(lambda values: _st.lists(values).map(tuple))),
        max_leaves=MAX_RECURSION_DEPTH
)
_comparable_values_categories |= _st.lists(_comparable_values_categories).map(
        lambda variants: _st.tuples(*variants)
)

equatable_empty_factories = (
        _st.sampled_from([bool, type(None), int, float, complex, str, bytes,
                          bytearray, list, tuple, dict, set, frozenset])
        | _st.builds(lambda value: (lambda: value), equatable_values)
)
equatable_pure_maps = (
        _st.sampled_from([lambda value: value, dir, id, repr, str])
        | _st.builds(lambda value: (lambda _: value), equatable_values)
)
nones = _st.builds(_None)
somes = _st.builds(_Some, equatable_values)
options = nones | somes
comparable_options = nones | _st.builds(_Some, comparable_values)
comparable_somes_categories = _comparable_values_categories.map(
        partial(_st.builds, _Some)
)
comparable_options_categories = comparable_somes_categories.map(
        lambda somes: nones | somes
)
comparable_options_pairs = comparable_options_categories.flatmap(
        lambda values: _st.tuples(values, values)
)
comparable_options_triplets = comparable_options_categories.flatmap(
        lambda values: _st.tuples(values, values, values)
)
options_maps = _st.builds(lambda value: (lambda _: value), options)
options_empty_factories = _st.builds(lambda value: (lambda: value), options)
lossless_representable_options = (nones
                                  | lossless_representable_values.map(_Some))
