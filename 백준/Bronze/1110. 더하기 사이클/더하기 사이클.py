N = input()
a = 100
c = 0
e = N
if len(N) == 1:
    N = '0' + N
while True:

    if  int(e) != int(a):
        b = int(N[0]) + int(N)%10
        a = f'{int(N)%10}' + f'{int(b)%10}'
        c += 1
        N = a
    else:
        print(c)
        break