from hypothesis import strategies as _st

from rustpy.option import (None_ as _None,
                           Some as _Some)
from tests.strategies import (comparable_values_categories,
                              equatable_values,
                              losslessly_representable_values)

equatable_empty_factories = (
        _st.sampled_from([bool, type(None), int, float, complex, str, bytes,
                          bytearray, list, tuple, dict, set, frozenset])
        | _st.builds(lambda value: (lambda: value), equatable_values)
)
equatable_pure_maps = (
        _st.sampled_from([lambda value: value, dir, id, repr, str])
        | _st.builds(lambda value: (lambda _: value), equatable_values)
)
options_types = _st.sampled_from([_None, _Some])
nones = _st.builds(_None)
equatable_somes = equatable_values.map(_Some)
equatable_options = nones | equatable_somes
comparable_options = nones | comparable_values_categories.flatmap(
        lambda values: values.map(_Some)
)
comparable_options_categories = comparable_values_categories.map(
        lambda values: nones | values.map(_Some)
)
comparable_options_pairs = comparable_options_categories.flatmap(
        lambda values: _st.tuples(values, values)
)
comparable_options_triplets = comparable_options_categories.flatmap(
        lambda values: _st.tuples(values, values, values)
)
options_maps = equatable_options.map(lambda value: (lambda _: value))
options_empty_factories = equatable_options.map(lambda value: (lambda: value))
losslessly_representable_options = (
        nones | losslessly_representable_values.map(_Some)
)
messages = _st.text()
