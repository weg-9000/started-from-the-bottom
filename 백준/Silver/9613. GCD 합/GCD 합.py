import sys
def gcd(a,b):
  while b > 0:
      a , b = b, a%b
  return a

N = int(input())
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    b = 0
    for i in range(1,len(a)):
      for j in range(1+i,len(a)):
        b += gcd(a[i],a[j])
    print(b)
