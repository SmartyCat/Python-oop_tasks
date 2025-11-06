from typing import Iterable


# first solution
def inversions(sequence: Iterable) -> int:
    result = 0
    for index, item in enumerate(sequence):
        for j in sequence[index + 1 :]:
            if item > j:
                result += 1
    else:
        return result


# second solution
def inversions(sequence: Iterable) -> int:
    return sum(
        1
        for index, item in enumerate(sequence)
        for i in sequence[index + 1 :]
        if item > i
    )


sequence = [3, 1, 4, 2]
print(inversions(sequence))

sequence = [1, 2, 3, 4, 5]
print(inversions(sequence))
sequence = [4, 3, 2, 1]
print(inversions(sequence))

sequence = [1, 1, 1, 1, 1, 1]
print(inversions(sequence))
