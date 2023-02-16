from __future__ import annotations

import math as _math
import typing as _t

import typing_extensions as _te

from .bool_ import bool_ as _bool
from .ordered import OrderedWrapper as _OrderedWrapper
from .utils import (floor_division_quotient as _floor_division_quotient,
                    floor_division_remainder as _floor_division_remainder,
                    trunc_division_quotient as _trunc_division_quotient,
                    trunc_division_remainder as _trunc_division_remainder)


class BaseFloat(_OrderedWrapper[float]):
    def __new__(cls, _value: float) -> _te.Self:
        if not isinstance(_value, float):
            raise TypeError(type(_value))
        self = super().__new__(cls)
        self._value = _value
        return self

    def abs(self) -> _te.Self:
        return type(self)(abs(self._value))

    def add(self, other: _te.Self) -> _te.Self:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        return type(self)(self._value + other._value)

    def ceil(self) -> _te.Self:
        fractional_part, whole_part = _math.modf(self._value)
        value = whole_part + _math.ceil(fractional_part)
        return type(self)(value)

    def div(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(divisor))
        return type(self)((_math.nan
                           if self._value == 0.0
                           else _math.copysign(_math.inf,
                                               self._value * divisor._value))
                          if divisor._value == 0.0
                          else _trunc_division_quotient(self._value,
                                                        divisor._value))

    def div_euclid(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(divisor))
        return type(self)((_math.nan
                           if self._value == 0.0
                           else _math.copysign(_math.inf,
                                               self._value * divisor._value))
                          if divisor._value == 0.0
                          else _floor_division_quotient(self._value,
                                                        divisor._value))

    def floor(self) -> _te.Self:
        fractional_part, whole_part = _math.modf(self._value)
        value = whole_part + _math.floor(fractional_part)
        return type(self)(value)

    def fract(self) -> _te.Self:
        value, _ = _math.modf(self._value)
        return type(self)(value)

    def is_finite(self) -> _bool:
        return _bool(_math.isfinite(self._value))

    def is_infinite(self) -> _bool:
        return _bool(_math.isinf(self._value))

    def is_nan(self) -> _bool:
        return _bool(_math.isnan(self._value))

    def mul(self, other: _te.Self) -> _te.Self:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        return type(self)(self._value * other._value)

    def rem(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(self))
        return type(self)(_math.nan
                          if divisor._value == 0.0
                          else _trunc_division_remainder(self._value,
                                                         divisor._value))

    def rem_euclid(self, divisor: _te.Self) -> _te.Self:
        if not isinstance(divisor, type(self)):
            raise TypeError(type(self))
        return type(self)(_math.nan
                          if divisor._value == 0.0
                          else _floor_division_remainder(self._value,
                                                         divisor._value))

    def round(self) -> _te.Self:
        fractional_part, whole_part = _math.modf(self._value)
        value = whole_part
        if abs(fractional_part) * 2.0 >= 1:
            value += 1.0 if fractional_part > 0.0 else -1.0
        return type(self)(value)

    def sub(self, other: _te.Self) -> _te.Self:
        if not isinstance(other, type(self)):
            raise TypeError(type(other))
        return type(self)(self._value - other._value)

    def trunc(self) -> _te.Self:
        _, value = _math.modf(self._value)
        return type(self)(value)

    @_t.overload
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _t.Any) -> _t.Any:
        ...

    def __add__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value + other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __mod__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mod__(self, other: _t.Any) -> _t.Any:
        ...

    def __mod__(self, other: _t.Any) -> _t.Any:
        return (type(self)(_math.nan
                           if other._value == 0.0
                           else _trunc_division_remainder(self._value,
                                                          other._value))
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mul__(self, other: _t.Any) -> _t.Any:
        ...

    def __mul__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value * other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    def __neg__(self) -> _te.Self:
        return type(self)(-self._value)

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}({self._value})'

    def __str__(self) -> str:
        return f'{self._value}{type(self).__qualname__}'

    @_t.overload
    def __sub__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _t.Any) -> _t.Any:
        ...

    def __sub__(self, other: _t.Any) -> _t.Any:
        return (type(self)(self._value - other._value)
                if isinstance(other, type(self))
                else NotImplemented)

    @_t.overload
    def __truediv__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __truediv__(self, other: _t.Any) -> _t.Any:
        ...

    def __truediv__(self, other: _t.Any) -> _t.Any:
        return (type(self)((_math.nan
                            if self._value == 0.0
                            else _math.copysign(_math.inf,
                                                self._value * other._value))
                           if other._value == 0.0
                           else _trunc_division_quotient(self._value,
                                                         other._value))
                if isinstance(other, type(self))
                else NotImplemented)
