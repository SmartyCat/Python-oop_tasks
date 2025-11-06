from typing import Callable, Iterable


def quantify(iterable: Iterable, predict: Callable) -> int:
    return sum(bool(i) if predict is None else predict(i) for i in iterable)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x > 1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x % 2 == 0))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, None))
