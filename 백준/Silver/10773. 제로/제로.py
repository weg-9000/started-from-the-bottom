N = int(input())
b = []
for _ in range(N):
    a = int(input())
    if a == 0:
        b.pop()
    else:
        b.append(a)
print(sum(b))