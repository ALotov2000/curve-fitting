from typing import Callable, List
from time import time
def show_time(f: Callable[List[any], any]):
    def inner(*args, **kwargs):
        if 'do_print' in kwargs.keys() and not kwargs['do_print']:
            f(*args, **kwargs)
        else:
            t0 = time()
            f(*args, **kwargs)
            t1 = time()
            print(f"function {f.__name__} took {t1 - t0} ms")
    return inner