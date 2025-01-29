N= int(input())
n=1003001
a = [False,False] + [True]*(n-1)
b=[]
for i in range(0,n+1):
    if a[i]:
        b.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
for k in range(0,len(b)+1):
    c = f'{b[k]}'
    if c == c[::-1] and b[k] >= N:
        print(c)
        break