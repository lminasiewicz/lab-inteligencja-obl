import time
from typing import Callable

# time measuring decorator
def measure_time(rounding_precision: None|int = None, return_solution: bool = False) -> Callable:
    def deco_measure_time(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> float:
            start = time.time()
            func_res = func(*args, **kwargs)
            elapsed = time.time() - start
            if rounding_precision is not None:
                elapsed = round(elapsed, rounding_precision)
            print(f"Function {func.__name__} executed in {elapsed}ms")
            if return_solution: 
                return func_res
            return elapsed
        return wrapper
    return deco_measure_time