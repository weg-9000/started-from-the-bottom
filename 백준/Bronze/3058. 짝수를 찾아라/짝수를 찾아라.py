a = int(input())
c = []
sum = 0
for _ in range(a):
    b = list(map(int,input().split(" ")))
    for j in range(len(b)):
        if b[j]%2 == 0:
            c.append(b[j])
    for k in c:
        sum += int(k)
    print(sum, min(c))
    c = []
    sum = 0