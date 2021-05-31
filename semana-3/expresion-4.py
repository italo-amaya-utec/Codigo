import math
a = float(input())
b = float(input())

rsp = (b == math.floor(a)) or a*b > 10

print(int(rsp))
