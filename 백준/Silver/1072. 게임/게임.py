N, M = map(int, input().split())
Z = (100*M)//N
Start = 0
T = N
X_1 = 0
if Z>=99:
    print(-1)
else:
    while Start <= T: 
        mid=(Start+T)//2 

        if (100*(M+mid))//(N+mid) <= Z:
            Start=mid+1 

        else: 
            X_1=mid 
            T=mid-1

    print(X_1)