from collections import deque
N, M = map(int, input().split())
a = deque()
b = []
for i in range(1,N+1):
    a.append(i)
while len(a) != 0:
  for _ in range(M-1):
    a.rotate(-1)
  b.append(str(a.popleft()))
print(f'<{', '.join(b)}>')