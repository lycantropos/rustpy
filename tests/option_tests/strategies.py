from hypothesis import strategies as _st

from rustpy.option import None_, Some

hashable_equatable_values = (
        _st.none() | _st.sampled_from([Ellipsis, NotImplemented])
        | _st.booleans() | _st.integers() | _st.fractions()
        | _st.floats(allow_nan=False) | _st.complex_numbers(allow_nan=False)
        | _st.binary() | _st.text() | _st.dates() | _st.datetimes()
)
hashable_equatable_values |= _st.recursive(hashable_equatable_values,
                                           _st.frozensets,
                                           max_leaves=5)
equatable_values = (
        hashable_equatable_values | _st.sets(hashable_equatable_values)
        | _st.recursive(hashable_equatable_values,
                        lambda strategy: _st.lists(strategy).map(tuple),
                        max_leaves=5)
)
deferred_equatable_values = _st.deferred(lambda: equatable_values)
equatable_values |= _st.recursive(
        deferred_equatable_values,
        lambda strategy: _st.lists(strategy) | _st.lists(strategy).map(tuple),
        max_leaves=5
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
options_maps = _st.builds(lambda value: (lambda _: value), options)
equatable_values |= options
