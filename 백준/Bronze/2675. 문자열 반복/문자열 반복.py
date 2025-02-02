N = int(input())
c = ''
for _ in range(N):
    a , b = map(str, input().split(" "))
    for i in range(len(b)):
        c += b[i]*int(a)
    print(c)
    c = ''