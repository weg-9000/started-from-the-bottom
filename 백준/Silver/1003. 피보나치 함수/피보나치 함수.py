def fiboZERO(N):
    a, b = 0, 1
    if N == 1:
      return 0
    else:
      for _ in range(3,N+1):
        a, b = b, a+b
      return b
def fiboONE(N):
    a, b = 1, 1
    if N == 0:
       return 0
    else:
      for _ in range(3,N+1):
        a, b = b, a+b
      return b
    
M = int(input())
for i in range(M):
  N = int(input())
  print(fiboZERO(N), fiboONE(N))