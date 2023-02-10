from hypothesis import strategies as _st

from rustpy.option import None_, Some

hashable_values = (_st.none() | _st.booleans() | _st.integers()
                   | _st.fractions() | _st.floats() | _st.complex_numbers()
                   | _st.binary() | _st.text() | _st.dates() | _st.datetimes())
hashable_values |= _st.recursive(hashable_values, _st.frozensets)
values = (hashable_values | _st.sets(hashable_values)
          | _st.recursive(hashable_values,
                          lambda strategy: _st.lists(strategy).map(tuple)))
deferred_values = _st.deferred(lambda: values)
values |= _st.recursive(
        deferred_values,
        lambda strategy: _st.lists(strategy) | _st.lists(strategy).map(tuple)
)
values |= _st.dictionaries(hashable_values, deferred_values)
empty_factories = _st.builds(lambda value: (lambda: value), values)
nones = _st.builds(None_)
somes = _st.builds(Some, values)
options = nones | somes
values |= options
