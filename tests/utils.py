import typing as _t
from contextlib import contextmanager

import pytest

from rustpy import primitive

Primitive = _t.TypeVar('Primitive', primitive.bool_, primitive.f32,
                       primitive.f64, primitive.i128, primitive.i16,
                       primitive.i32, primitive.i64, primitive.i8,
                       primitive.isize, primitive.u128, primitive.u16,
                       primitive.u32, primitive.u64, primitive.u8,
                       primitive.usize)

_AnyBool = _t.Union[bool, primitive.bool_]


def equivalence(first: _AnyBool, second: _AnyBool) -> bool:
    return bool(first) is bool(second)


def implication(antecedent: _AnyBool, consequent: _AnyBool) -> bool:
    return not antecedent or bool(consequent)


@contextmanager
def not_raises(
        *exceptions: _t.Type[BaseException]
) -> _t.Generator[None, None, None]:
    try:
        yield
    except exceptions:
        raise pytest.fail('DID RAISE {}'.format(exceptions))
