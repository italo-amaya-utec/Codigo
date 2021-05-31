import math
a = float(input())
b = float(input())

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

rsp = (truncate(a,2) == b)

print(int(rsp))
