a, b = map(int, input().split())
c = 0
while a != b:
    if a > b:
        a = a - b
        c += 1
    else:
        b = b - a 
        c +=1
print(c)