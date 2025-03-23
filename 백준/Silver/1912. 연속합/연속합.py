N = int(input())
M = list(map(int, input().split()))

A = [0] * N  
A[0] = M[0]

for i in range(1, N):
    A[i] = A[i-1] + M[i]

min_pre = 0 
max_sum = A[0]

for j in range(N):
    max_sum = max(max_sum, A[j] - min_pre)
    min_pre = min(min_pre, A[j])

print(max_sum)