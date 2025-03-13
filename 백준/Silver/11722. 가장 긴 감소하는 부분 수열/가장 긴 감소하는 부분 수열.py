N = int(input())
M = [0] + list(map(int, input().split()))
A = [0]*(N+1)

for i in range(1, N+1):
    B = 0
    for j in  range(0,i):
        if M[i] < M[j]:
            B = max(B, A[j])
    A[i] = B + 1
print(max(A))