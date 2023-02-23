import sys
import types
import typing as _t
from contextlib import contextmanager as _contextmanager

import pytest as _pytest
from hypothesis import strategies as _st
from hypothesis.strategies import SearchStrategy as _SearchStrategy

from rustpy import primitive as _primitive

Float = _t.TypeVar('Float', _primitive.f32, _primitive.f64)
Integer = _t.TypeVar('Integer', _primitive.i128, _primitive.i16,
                     _primitive.i32, _primitive.i64, _primitive.i8,
                     _primitive.isize, _primitive.u128, _primitive.u16,
                     _primitive.u32, _primitive.u64, _primitive.u8,
                     _primitive.usize)
Numeric = _t.TypeVar('Numeric', _primitive.f32, _primitive.f64,
                     _primitive.i128, _primitive.i16, _primitive.i32,
                     _primitive.i64, _primitive.i8, _primitive.isize,
                     _primitive.u128, _primitive.u16, _primitive.u32,
                     _primitive.u64, _primitive.u8, _primitive.usize)
Primitive = _t.TypeVar('Primitive', _primitive.bool_, _primitive.f32,
                       _primitive.f64, _primitive.i128, _primitive.i16,
                       _primitive.i32, _primitive.i64, _primitive.i8,
                       _primitive.isize, _primitive.u128, _primitive.u16,
                       _primitive.u32, _primitive.u64, _primitive.u8,
                       _primitive.usize)
if sys.version_info < (3, 9):
    SpecializationTypes = (type(_t.List[int]),)
else:
    SpecializationTypes = (types.GenericAlias, type(_t.List[int]))
_AnyBool = _t.Union[bool, _primitive.bool_]


def equivalence(first: _AnyBool, second: _AnyBool) -> bool:
    return bool(first) is bool(second)


def implication(antecedent: _AnyBool, consequent: _AnyBool) -> bool:
    return not antecedent or bool(consequent)


@_contextmanager
def not_raises(
        *exceptions: _t.Type[BaseException]
) -> _t.Generator[None, None, None]:
    try:
        yield
    except exceptions:
        raise _pytest.fail('DID RAISE {}'.format(exceptions))


def rust_int_to_python_int(value: Integer) -> int:
    return int(value)


_T = _t.TypeVar('_T')


def to_homogeneous_tuples(
        values: _SearchStrategy[_T]
) -> _SearchStrategy[_t.Tuple[_T, ...]]:
    return _st.lists(values).map(tuple)


def to_integers(integer_type: _t.Type[Integer]) -> _SearchStrategy[Integer]:
    return (_st.integers(rust_int_to_python_int(integer_type.MIN),
                         rust_int_to_python_int(integer_type.MAX))
            .map(integer_type))


def to_non_zero_integers(cls: _t.Type[Integer]) -> _SearchStrategy[Integer]:
    min_value = rust_int_to_python_int(cls.MIN)
    return (((_st.nothing() if min_value == 0 else _st.integers(min_value, -1))
             | _st.integers(1, rust_int_to_python_int(cls.MAX)))
            .map(cls))


def to_unit_integers(cls: _t.Type[Integer]) -> _SearchStrategy[Integer]:
    return _st.builds(cls, _st.just(1))


def to_zero_integers(cls: _t.Type[Integer]) -> _SearchStrategy[Integer]:
    return _st.builds(cls, _st.just(0))
