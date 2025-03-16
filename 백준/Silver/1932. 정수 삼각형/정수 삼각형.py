def solution(a):
    b = a   
    for i in range(1,N):
        for j in range(0,i+1):
            if j == 0:
                b[i][j] += b[i-1][j]
            elif j == i:
                b[i][j] += b[i-1][j-1]
            else:
                b[i][j] += max(b[i-1][j-1],b[i-1][j])
    return max(b[N-1])


N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
print(solution(a))