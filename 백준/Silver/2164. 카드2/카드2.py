from collections import deque
N = int(input())
q = deque()
a = []
for i in range(1,N+1):
    q.append(i)
while len(q) != 1:
    a.append(q.popleft())
    q.rotate(-1)
    if len(q) == 1:
      break
print(q.popleft())