try:
    from ._crustpy import (bool_,
                           f32,
                           f64,
                           i128,
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
    from ._rustpy.primitive import (bool_,
                                    f32,
                                    f64,
                                    i128,
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

bool_.__doc__ = (
    'Represents a value, which could only be either true or false. '
    'If you cast a bool into an integer, true will be 1 and false will be 0.'
)
f32.__doc__ = ('A 32-bit floating point type '
               '(specifically, the "binary32" type defined in IEEE 754-2008).')
f64.__doc__ = ('A 64-bit floating point type '
               '(specifically, the "binary64" type defined in IEEE 754-2008).')
i128.__doc__ = 'The 128-bit signed integer type.'
i64.__doc__ = 'The 64-bit signed integer type.'
i32.__doc__ = 'The 32-bit signed integer type.'
i16.__doc__ = 'The 16-bit signed integer type.'
i8.__doc__ = 'The 8-bit signed integer type.'
isize.__doc__ = 'The pointer-sized signed integer type.'
u128.__doc__ = 'The 128-bit unsigned integer type.'
u64.__doc__ = 'The 64-bit unsigned integer type.'
u32.__doc__ = 'The 32-bit unsigned integer type.'
u16.__doc__ = 'The 16-bit unsigned integer type.'
u8.__doc__ = 'The 8-bit unsigned integer type.'
usize.__doc__ = 'The pointer-sized unsigned integer type.'
