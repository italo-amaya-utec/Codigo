a = str(input())
b = str(input())
c = str(input())

rsp = (a > b) or ((b > c) and (a > c))

print(int(rsp))
