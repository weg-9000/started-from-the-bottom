def fibo(n):
    a, b = 1, 1
    for _ in range(3,n+1):
      a, b = b, a+b
    return b

def fibonacci(n):
   return n - 2
   

N = int(input())
print(fibo(N), fibonacci(N))