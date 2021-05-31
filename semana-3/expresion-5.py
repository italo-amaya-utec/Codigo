import math
a = int(input())
b = int(input())

rsp = not (math.sqrt(a**2 + b**2) == (2*a - b))

print(int(rsp))
