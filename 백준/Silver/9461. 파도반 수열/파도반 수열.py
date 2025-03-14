import sys
def p(a):
    if A[a]:
        return A[a]
    else:
        for _ in range(4,a+1):
            A[a] = p(a-2) + p(a-3)
        return A[a]
N = int(sys.stdin.readline())
A = [0,1,1,1] + [0]*(97)

for _ in range(N):
    a = int(sys.stdin.readline())
    print(p(a))