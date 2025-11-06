from re import fullmatch


def is_fraction(string: str) -> bool:
    return (
        fullmatch(r"-?\d+\/\d+", string) is not None
        and int(string[string.index("/") + 1 :]) != 0
    )


print(is_fraction("1000/1"))
print(is_fraction("-54/9"))
print(is_fraction("71"))
print(is_fraction("1 / 82"))
print(is_fraction("1/0"))
