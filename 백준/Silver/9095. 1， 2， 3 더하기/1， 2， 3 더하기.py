def solution(A):
  for i in range(3,A+1):
    B[i] = B[i-1] + B[i-2] + B[i-3]
  return B[A]



N = int(input())
for _ in range(N):
    A = int(input())
    B = [1, 1, 2] + [0]*(A-2)
    print(solution(A))