N = int(input())
C = [[0]*100 for _ in range(100)]
for i in range(N):
    A, B = map(int, input().split(" "))
    
    for j in range(A,A + 10):
        for k in range(B,B + 10):
            C[j][k] = 1
s = 0
for l in range(100):
    s += C[l].count(1)
print(s)