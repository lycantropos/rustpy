try:
    from rustpy._crustpy import (f32,
                                 f64)
except ImportError:
    from rustpy._rustpy.primitive.f32 import f32
    from rustpy._rustpy.primitive.f64 import f64
