N = input().split(" ")
a = 0
for i in N:
    a += int(i)**2
print(int(a%10))