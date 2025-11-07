from typing import Any


def pluck(data: dict, path: str, default: Any = None) -> Any:
    for p in path.split("."):
        if p in data:
            data = data[p]
        else:
            return default
    else:
        return data


d = {"a": {"b": {"c": {"d": {"e": 4}}}}}
print(pluck(d, "a.b.c"))
d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
print(pluck(d, "x"))
d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
print(pluck(d, "a.o"))
