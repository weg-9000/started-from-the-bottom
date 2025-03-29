import bisect
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
C = {}

for i in A:
  if i not in C:
    C[i] = 1
  else:
    C[i] += 1


for j in B:
    if A[bisect.bisect(A,j)-1]==j:
        print(C[j], end=' ')
    else:
        print(0, end=' ')
