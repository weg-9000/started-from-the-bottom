N = int(input())
M = int(input())
A = list(map(int, input().split()))

if N <= sum(A):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")