import sys
import json
from re import findall


# first solution with regex
for i in sys.stdin.readlines():
    x, y = map(float, (findall(r"\-?\d+(?:\.\d+)?", i)))
    print(-90 <= x <= 90 and -180 <= y <= 180)

# second solution with string methods
for i in sys.stdin.readlines():
    x, y = map(float, i.replace("(", "").replace(")", "").rstrip().split(", "))
    print(-90 <= x <= 90 and -180 <= y <= 180)
