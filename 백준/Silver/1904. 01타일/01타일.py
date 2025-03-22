def solution(A):
  for i in range(3,A+1):
    B[i] = (B[i-1] + B[i-2])%15746
  return B[A]




A = int(input())
B = [0, 1, 2] + [0]*(A-2)
print(solution(A))