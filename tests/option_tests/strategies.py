from functools import partial

from hypothesis import strategies as _st

from rustpy.option import (None_,
                           Some)

MAX_RECURSION_DEPTH = 3

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
comparable_values_categories = _st.recursive(
        _st.sampled_from(comparable_values_categories_tuple),
        lambda category:
        (category.map(_st.lists)
         | category.map(lambda values: _st.lists(values).map(tuple))),
        max_leaves=MAX_RECURSION_DEPTH
)
comparable_values_categories |= _st.lists(comparable_values_categories).map(
        lambda variants: _st.tuples(*variants)
)
hashable_equatable_values = (
        _st.none() | _st.sampled_from([Ellipsis, NotImplemented])
        | _st.booleans() | _st.integers() | _st.fractions()
        | _st.floats(allow_nan=False) | _st.complex_numbers(allow_nan=False)
        | _st.binary() | _st.text() | _st.dates() | _st.datetimes()
)
hashable_equatable_values |= _st.recursive(hashable_equatable_values,
                                           _st.frozensets,
                                           max_leaves=MAX_RECURSION_DEPTH)
equatable_values = (
        hashable_equatable_values | _st.sets(hashable_equatable_values)
        | _st.recursive(hashable_equatable_values,
                        lambda strategy: _st.lists(strategy).map(tuple),
                        max_leaves=MAX_RECURSION_DEPTH)
)
deferred_equatable_values = _st.deferred(lambda: equatable_values)
equatable_values |= _st.recursive(
        deferred_equatable_values,
        lambda strategy: _st.lists(strategy) | _st.lists(strategy).map(tuple),
        max_leaves=MAX_RECURSION_DEPTH
)
equatable_values |= _st.dictionaries(hashable_equatable_values,
                                     deferred_equatable_values)
equatable_empty_factories = (
        _st.sampled_from([bool, type(None), int, float, complex, str, bytes,
                          bytearray, list, tuple, dict, set, frozenset])
        | _st.builds(lambda value: (lambda: value), equatable_values)
)
equatable_pure_maps = (
        _st.sampled_from([lambda value: value, dir, id, repr, str])
        | _st.builds(lambda value: (lambda _: value), equatable_values)
)
nones = _st.builds(None_)
somes = _st.builds(Some, deferred_equatable_values)
options = nones | somes
comparable_options = nones | _st.builds(Some, comparable_values)
comparable_somes_categories = comparable_values_categories.map(
        partial(_st.builds, Some)
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
equatable_values |= options
