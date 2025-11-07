from typing import Iterable


def annual_return(start: int, percent: int, years: int) -> Iterable:
    for _ in range(years):
        start += (start * percent) / 100
        yield start


for value in annual_return(70000, 8, 10):
    print(round(value))
