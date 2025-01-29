A = []
for _ in range(5):
    a = int(input())
    A.append(a)
print(f'{min(A[:3]) + min(A[3:]) - 50}')