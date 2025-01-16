N = [i for i in range(1,31)]
for i in range(28):
    A = int(input())
    N.remove(A)
print(min(N))
print(max(N))