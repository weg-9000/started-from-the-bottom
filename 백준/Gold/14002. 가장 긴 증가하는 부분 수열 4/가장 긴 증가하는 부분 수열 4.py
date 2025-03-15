N = int(input())
M = list(map(int, input().split()))
A = [[] for _ in range(max(M)+1)]
for i in M:   
    A[i] = max(A[:i], key= lambda x : len(x)) + [i]
B = max(A, key = lambda x : len(x))  
print(len(B))
print(*B)