from __future__ import annotations

from .bool_ import bool_ as _bool
from .ordered import OrderedWrapper as _OrderedWrapper


class BaseFloat(_OrderedWrapper[float]):
    def __bool__(self) -> bool:
        raise TypeError(f'Expected `{_bool.__qualname__}`, '
                        f'found `{type(self).__qualname__}`.')

    def __str__(self) -> str:
        return f'{self._value}{type(self).__qualname__}'
