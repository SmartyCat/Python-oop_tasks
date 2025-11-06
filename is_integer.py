from re import findall


# solution with regex
def is_integer(string: str) -> bool:
    result = findall(r"^-?\d+$", string)
    return True if result and result[0] == string else False


# solution with string methods
def is_integer(string: str) -> bool:
    return string.lstrip("-").isdigit()


print(is_integer("199"))

print(is_integer("-43"))
print(is_integer("5f"))
print(is_integer("5.0"))
print(is_integer("1.1"))
