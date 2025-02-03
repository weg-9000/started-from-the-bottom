N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
 
    while b > 0:
        a , b = b, a%b
    print(a)