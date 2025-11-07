from functools import wraps
from typing import Callable, Any


def recviz(func: Callable) -> str:
    n = -4

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        nonlocal n
        n += 4
        print(
            " " * n
            + f"-> {func.__name__}({", ".join([str(a) for a in args]+[str(k)+"="+str(kwargs[k]) for k in kwargs])})"
        )
        result = func(*args, **kwargs)
        print(" " * n + f"<- {str(result)}")
        n -= 4
        return result

    return wrapper


@recviz
def add(a, b):
    return a + b


add(1, b=2)


@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)


add("a", b="b", c="c", d=3, e=True)


@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)


@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)
