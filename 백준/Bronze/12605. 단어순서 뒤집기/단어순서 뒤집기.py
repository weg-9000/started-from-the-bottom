N = int(input())
for i in range(N):
  a = input().split(" ")
  print(f'Case #{i+1}: {" ".join(a[::-1])}')