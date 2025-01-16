N = int(input())
A = list(map(int, input().split(" ")))
V = int(input())
B = 0
for i in range(N):
    if A[i] == V:
        B += 1
print(B)