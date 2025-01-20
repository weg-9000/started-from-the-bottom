a, b = map(int, input().split(" "))
c = int(input())
if (b+c)//60 != 0:
    a = a + (b+c)//60
    b = (b + c)%60
    if a//24 == 1:
        a = a%24
else:
    b += c
print(f'{a} {b}')