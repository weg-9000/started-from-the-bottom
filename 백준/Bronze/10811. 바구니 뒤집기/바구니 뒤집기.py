N, M = map(int, input().split(" "))
A = []
B = []
for i in range(1,N+1):
        A.append(i)
for j in range(M):
    a, b = map(int, input().split(" "))
    B = A[a-1:b]
    B.reverse()
    A[a-1:b] = B
print(*A)