from __future__ import annotations

from rustpy.primitive.bool_ import bool_
from .ordered import _OrderedWrapper


class BaseFloat(_OrderedWrapper[float]):
    def __bool__(self) -> bool:
        raise TypeError(f'Expected `{bool_.__qualname__}`, '
                        f'found `{type(self).__qualname__}`.')

    def __str__(self) -> str:
        return f'{self._value}{type(self).__qualname__}'
