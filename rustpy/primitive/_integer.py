try:
    from rustpy._crustpy import (i128,
                                 i16,
                                 i32,
                                 i64,
                                 i8,
                                 isize,
                                 u128,
                                 u16,
                                 u32,
                                 u64,
                                 u8,
                                 usize)
except ImportError:
    from rustpy._rustpy.primitive.i128 import i128
    from rustpy._rustpy.primitive.i16 import i16
    from rustpy._rustpy.primitive.i32 import i32
    from rustpy._rustpy.primitive.i64 import i64
    from rustpy._rustpy.primitive.i8 import i8
    from rustpy._rustpy.primitive.isize import isize
    from rustpy._rustpy.primitive.u16 import u16
    from rustpy._rustpy.primitive.u128 import u128
    from rustpy._rustpy.primitive.u32 import u32
    from rustpy._rustpy.primitive.u64 import u64
    from rustpy._rustpy.primitive.u8 import u8
    from rustpy._rustpy.primitive.usize import usize
