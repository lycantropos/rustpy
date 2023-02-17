from hypothesis import strategies as _st

from rustpy.result import (Err,
                           Ok)
from tests.strategies import equatable_values

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
equatable_pure_maps = (
        _st.sampled_from([lambda value: value, dir, id, repr, str])
        | _st.builds(lambda value: (lambda _: value), equatable_values)
)
errs = _st.builds(Err, equatable_values)
oks = _st.builds(Ok, equatable_values)
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
