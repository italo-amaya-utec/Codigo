a = int(input())
b = int(input())

rsp = not ((a == b or a <= b) and ((a%b) != 2))

print(int(rsp))
