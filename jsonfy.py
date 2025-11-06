from typing import Callable, Any
from functools import wraps
import json


def jsonify(func: Callable) -> str:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return json.dumps(func(*args, **kwargs))

    return wrapper


@jsonify
def make_user(id, live, options):
    return {"id": id, "live": live, "options": options}


print(make_user(4, False, None))


@jsonify
def make_list(n):
    return list(range(1, n + 1))


print(make_list(10))


@jsonify
def make_str(s1, s2):
    return (s1 + s2) * 5


print(make_str("bee", "geek"))
