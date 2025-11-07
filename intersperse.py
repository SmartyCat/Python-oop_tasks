from typing import Iterable, Any


# Решение номер один  в лоб
def intersperse(iterable: Iterable, delimiter: Any) -> Iterable:
    new = []
    for item in iterable:
        new.append(item)
        new.append(delimiter)
    else:
        yield from new if new[-1] != delimiter else new[:-1]


# Решение номер два, экономнее по памяти
def intersperse(iterable: Iterable, delimiter: Any) -> Iterable:
    iterable = iter(iterable)
    item = next(iterable)
    while True:
        yield item
        try:
            item = next(iterable)
            yield delimiter
        except StopIteration:
            break


print(*intersperse([1, 2, 3], 0))
inter = intersperse("beegeek", "!")
print(next(inter))
print(next(inter))
print(*inter)
print(*intersperse("A", "..."))
