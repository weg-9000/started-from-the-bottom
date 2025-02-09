import math
N = int(input())
M = list(map(int, input().split()))
for i in range(1,N):
  print(f"{int(M[0]/math.gcd(M[0],M[i]))}/{int(M[i]/math.gcd(M[0],M[i]))}")