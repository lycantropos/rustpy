from hypothesis import strategies as _st

from rustpy.result import (Err,
                           Ok)

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
equatable_pure_maps = (
        _st.sampled_from([lambda value: value, dir, id, repr, str])
        | _st.builds(lambda value: (lambda _: value), equatable_values)
)
errs = _st.builds(Err, deferred_equatable_values)
oks = _st.builds(Ok, deferred_equatable_values)
results = errs | oks
comparable_results = (_st.builds(Err, comparable_values)
                      | _st.builds(Ok, comparable_values))
comparable_results_categories = comparable_values_categories.map(
        lambda category: _st.builds(Err, category) | _st.builds(Ok, category)
)
comparable_results_pairs = comparable_results_categories.flatmap(
        lambda values: _st.tuples(values, values)
)
comparable_results_triplets = comparable_results_categories.flatmap(
        lambda values: _st.tuples(values, values, values)
)
results_maps = _st.builds(lambda value: (lambda _: value), results)
equatable_values |= results
