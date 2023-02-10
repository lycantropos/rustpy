from __future__ import annotations

import operator as _operator
import typing as _t


def ceil_division_quotient(dividend: _t.Any, divisor: _t.Any) -> _t.Any:
    return -((-dividend) // divisor)


def ceil_division_remainder(dividend: _t.Any, divisor: _t.Any) -> _t.Any:
    return -((-dividend) % divisor)


floor_division_remainder = _operator.mod
floor_division_quotient = _operator.floordiv


def trunc_division_quotient(dividend: _t.Any, divisor: _t.Any) -> _t.Any:
    return (floor_division_quotient(dividend, divisor)
            if ((dividend < 0) is (divisor < 0))
            else ceil_division_quotient(dividend, divisor))


def trunc_division_remainder(dividend: _t.Any, divisor: _t.Any) -> _t.Any:
    return (floor_division_remainder(dividend, divisor)
            if ((dividend < 0) is (divisor < 0))
            else ceil_division_remainder(dividend, divisor))
