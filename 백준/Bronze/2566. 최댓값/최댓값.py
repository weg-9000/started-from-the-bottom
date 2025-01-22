b = []
C = []
for i in range(9):
    A = list(map(int, input().split(" ")))
    b.append(A)
for j in range(len(b)):
    C.append(max(b[j]))
print(max(C))
c = C.index(max(C))
print(c+1, b[c].index(max(C))+1)