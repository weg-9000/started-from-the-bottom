A, B = input().strip(), input().strip()
N, M = len(A), len(B)

C = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1] == B[j-1]:
            C[i][j] = C[i-1][j-1] + 1
        else:
            C[i][j] = max(C[i-1][j], C[i][j-1])
print(C[-1][-1])