N, M = map(int, input().split(" "))
a = [False,False] + [True]*(M-1)
for i in range(N-N,M+1):
    if a[i]:
        if i>=N:
            print(i , end = "\n")
        for j in range(2*i, M+1, i):
            a[j] = False