N = int(input())
M = list(map(int, input().split()))
A = [1]*(N)
C = [1]*(N)
for i in range(0, N):
    for j in  range(0,i):
        if M[i] > M[j]:
          A[i] = max(A[i],A[j]+1)


for k in range(N,-1,-1):
    for w in range(N-1,k,-1):
        if M[k] > M[w]:
           C[k] = max(C[k],C[w]+1)
B = [0]*N
for f in range(N):
    B[f] = A[f] + C[f] - 1
print(max(B))
    