try:
    from rustpy._crustpy import bool_
except ImportError:
    from rustpy._rustpy.primitive.bool_ import bool_
