import math
a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))

N = a*d +c*b
M = d*b
print(f"{int(N/math.gcd(N,M))} {int(M/math.gcd(N,M))}")