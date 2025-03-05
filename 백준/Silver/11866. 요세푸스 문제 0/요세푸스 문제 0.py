from collections import deque
N, M = map(int, input().split())
a = deque()
b = []
for i in range(1,N+1):
    a.append(i)
while len(a) != 0:
  a.rotate(-M)
  b.append(str(a.pop()))
print(f'<'+', '.join(b)+'>')