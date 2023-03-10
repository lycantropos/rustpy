import sys
from typing import (Tuple,
                    Type)

from hypothesis import given

from rustpy.primitive import (f64,
                              i32,
                              u32)
from tests.utils import (Float,
                         implication)
from . import strategies


@given(strategies.float_types)
def test_epsilon(float_type: Type[Float]) -> None:
    one = float_type(1.0)

    assert float_type.EPSILON is float_type.EPSILON
    assert isinstance(float_type.EPSILON, float_type)
    assert float_type.EPSILON + one != one
    assert float_type.EPSILON / float_type(2.0) + one == one


@given(strategies.float_types_with_values)
def test_infinity(float_type_with_float: Tuple[Type[Float], Float]) -> None:
    float_type, float_ = float_type_with_float

    assert float_type.INFINITY is float_type.INFINITY
    assert isinstance(float_type.INFINITY, float_type)
    assert implication(not float_.is_nan(), float_type.INFINITY >= float_)


@given(strategies.float_types_with_values)
def test_nan(float_type_with_float: Tuple[Type[Float], Float]) -> None:
    float_type, float_ = float_type_with_float

    assert float_type.NAN is float_type.NAN
    assert isinstance(float_type.NAN, float_type)
    assert not float_type.NAN == float_
    assert not float_type.NAN >= float_
    assert not float_type.NAN > float_
    assert not float_type.NAN <= float_
    assert not float_type.NAN < float_
    assert float_type.NAN != float_


@given(strategies.float_types_with_values)
def test_neg_infinity(
        float_type_with_float: Tuple[Type[Float], Float]
) -> None:
    float_type, float_ = float_type_with_float

    assert float_type.NEG_INFINITY is float_type.NEG_INFINITY
    assert isinstance(float_type.NEG_INFINITY, float_type)
    assert implication(not float_.is_nan(), float_type.NEG_INFINITY <= float_)


@given(strategies.float_types_with_finite_values)
def test_max(float_type_with_float: Tuple[Type[Float], Float]) -> None:
    float_type, float_ = float_type_with_float

    assert float_type.MAX >= float_


@given(strategies.float_types_with_finite_values)
def test_min(float_type_with_float: Tuple[Type[Float], Float]) -> None:
    float_type, float_ = float_type_with_float

    assert float_type.MIN <= float_


def test_connection_with_sys_float_info() -> None:
    assert f64.DIGITS == u32(sys.float_info.dig)
    assert f64.EPSILON == f64(sys.float_info.epsilon)
    assert f64.MANTISSA_DIGITS == u32(sys.float_info.mant_dig)
    assert f64.MAX == f64(sys.float_info.max)
    assert f64.MAX_10_EXP == i32(sys.float_info.max_10_exp)
    assert f64.MAX_EXP == i32(sys.float_info.max_exp)
    assert f64.MIN == f64(-sys.float_info.max)
    assert f64.MIN_10_EXP == i32(sys.float_info.min_10_exp)
    assert f64.MIN_EXP == i32(sys.float_info.min_exp)
    assert f64.MIN_POSITIVE == f64(sys.float_info.min)
    assert f64.RADIX == u32(sys.float_info.radix)
