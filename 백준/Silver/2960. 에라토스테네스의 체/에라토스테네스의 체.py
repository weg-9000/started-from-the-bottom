N, K = map(int, input().split(" "))
A = [False,False] + [True]*(N-1)
B = 0
for i in range(2,N+1):
    if A[i]:
        for j in range(i, N+1, i):
            if A[j]:
                A[j] = False
                B += 1
                if B == K:
                    print(j)