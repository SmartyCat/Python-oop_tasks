def func(s: str) -> bool:
    flag = 0
    for i in s:
        flag += 1 if i == "(" else -1
        if flag < 0:
            return False
    return flag == 0


print(func(input()))
