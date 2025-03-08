from collections import deque
N = int(input())
T = int(input())
A = deque(input().split())
B = input().split()

for i in range(T):
    A.rotate(-int(B[i])+1)
    print(f'{A[0]}', end= ' ')