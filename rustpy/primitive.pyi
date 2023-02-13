import typing as _t

import typing_extensions as _te

from rustpy.option import Option


@_te.final
class bool_:
    def __init__(self, _value: bool) -> None:
        ...


class _BaseFloat(_te.Protocol):
    def __bool__(self) -> _t.NoReturn:
        ...

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __ge__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...


@_te.final
class f32(_BaseFloat):
    def __init__(self, _value: float) -> None:
        ...


@_te.final
class f64(_BaseFloat):
    def __init__(self, _value: float) -> None:
        ...


class _BaseInteger(_te.Protocol):
    BITS: _t.ClassVar[u32] = ...
    MAX: _t.ClassVar[_te.Self] = ...
    MIN: _t.ClassVar[_te.Self] = ...

    def add(self, other: _te.Self) -> _te.Self:
        ...

    def checked_add(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def checked_div(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def checked_div_euclid(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def checked_mul(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def checked_rem(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def checked_rem_euclid(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def checked_sub(self, other: _te.Self) -> Option[_te.Self]:
        ...

    def div(self, divisor: _te.Self) -> _te.Self:
        ...

    def div_euclid(self, divisor: _te.Self) -> _te.Self:
        ...

    def rem(self, divisor: _te.Self) -> _te.Self:
        ...

    def rem_euclid(self, divisor: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __add__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __and__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __and__(self, other: _t.Any) -> _t.Any:
        ...

    def __bool__(self) -> _t.NoReturn:
        ...

    @_t.overload
    def __eq__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __eq__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __ge__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __ge__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __gt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __gt__(self, other: _t.Any) -> _t.Any:
        ...

    def __init__(self, _value: int) -> None:
        ...

    def __invert__(self) -> _te.Self:
        ...

    @_t.overload
    def __le__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __le__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lt__(self, other: _te.Self) -> bool:
        ...

    @_t.overload
    def __lt__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __lshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __lshift__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __mod__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mod__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __mul__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __mul__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __rshift__(self, other: u32) -> _te.Self:
        ...

    @_t.overload
    def __rshift__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __sub__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __sub__(self, other: _t.Any) -> _t.Any:
        ...

    @_t.overload
    def __truediv__(self, other: _te.Self) -> _te.Self:
        ...

    @_t.overload
    def __truediv__(self, other: _t.Any) -> _t.Any:
        ...


class _BaseSignedInteger(_BaseInteger):
    def __neg__(self) -> _te.Self:
        ...


class _BaseUnsignedInteger(_BaseInteger):
    ...


@_te.final
class i128(_BaseSignedInteger):
    pass


@_te.final
class i16(_BaseSignedInteger):
    pass


@_te.final
class i32(_BaseSignedInteger):
    pass


@_te.final
class i64(_BaseSignedInteger):
    pass


@_te.final
class i8(_BaseSignedInteger):
    pass


@_te.final
class isize(_BaseSignedInteger):
    pass


@_te.final
class str_:
    pass


@_te.final
class u128(_BaseUnsignedInteger):
    pass


@_te.final
class u16(_BaseUnsignedInteger):
    pass


@_te.final
class u32(_BaseUnsignedInteger):
    pass


@_te.final
class u64(_BaseUnsignedInteger):
    pass


@_te.final
class u8(_BaseUnsignedInteger):
    pass


@_te.final
class usize(_BaseUnsignedInteger):
    pass
