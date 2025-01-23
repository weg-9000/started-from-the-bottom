A = []
B = []
D = {' '}
for _ in range(5):
    a = input()
    A.append(a)
C = max(len(j) for j in A)
for i in range(len(A)):
    if len(A[i]) < C:
        for _ in range(C-len(A[i])):
            A[i] += ' '
for l in range(C):
    for k in range(len(A)):
        B += A[k][l]
B = [f for f in B if f not in D]
print(*B,sep='')