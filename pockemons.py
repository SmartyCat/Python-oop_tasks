import sys
from collections import Counter

# first solution
data = Counter(sys.stdin.readlines())
print(sum(d - 1 for d in data.values()))

# second colution
result = 0
collects = []

for i in sys.stdin.readlines():
    if i not in collects:
        collects.append(i)
    else:
        result += 1
else:
    print(result)
