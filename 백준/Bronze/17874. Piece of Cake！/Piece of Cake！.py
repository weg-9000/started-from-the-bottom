n, h, v = map(int, input().split())
print(max(h * v, h * (n - v), (n - h) * v, (n - h) * (n - v))*4)