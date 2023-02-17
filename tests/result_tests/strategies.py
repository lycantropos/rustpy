from hypothesis import strategies as _st

from rustpy.result import (Err as _Err,
                           Ok as _Ok)
from tests.strategies import (
    comparable_values_categories as _comparable_values_categories,
    equatable_values as _equatable_values,
    lossless_representable_values as _lossless_representable_values
)

MAX_RECURSION_DEPTH = 3

equatable_pure_maps = (
        _st.sampled_from([lambda value: value, dir, id, repr, str])
        | _st.builds(lambda value: (lambda _: value), _equatable_values)
)
equatable_errs = _equatable_values.map(_Err)
equatable_oks = _equatable_values.map(_Ok)
equatable_results = equatable_errs | equatable_oks
comparable_results = _comparable_values_categories.flatmap(
        lambda values: _st.builds(_Err, values) | _st.builds(_Ok, values)
)
_comparable_results_categories = _comparable_values_categories.map(
        lambda category: _st.builds(_Err, category) | _st.builds(_Ok, category)
)
comparable_results_pairs = _comparable_results_categories.flatmap(
        lambda values: _st.tuples(values, values)
)
comparable_results_triplets = _comparable_results_categories.flatmap(
        lambda values: _st.tuples(values, values, values)
)
results_maps = _st.builds(lambda value: (lambda _: value), equatable_results)
lossless_representable_results = (
        _st.builds(_Err, _lossless_representable_values)
        | _st.builds(_Ok, _lossless_representable_values)
)
