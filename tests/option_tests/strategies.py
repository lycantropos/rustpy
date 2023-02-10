from hypothesis import strategies as _st

from rustpy.option import None_, Some

values = _st.from_type(object)
empty_factories = _st.builds(lambda value: (lambda: value), values)
nones = _st.builds(None_)
somes = _st.builds(Some, values)
options = nones | somes
