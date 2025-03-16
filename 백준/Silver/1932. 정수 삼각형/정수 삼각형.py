def solution(a):
    b = a[-1]
    for i in range(len(a)-2,-1,-1):
        for j in range(len(a[i])):
            b[j] = a[i][j] + max(b[j],b[j+1])
    return b[0]


N = int(input())
a = [[]]*N
for i in range(N):
    a[i] = list(map(int, input().split()))
print(solution(a))