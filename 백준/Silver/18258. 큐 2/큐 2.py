import sys
from collections import deque
s = int(sys.stdin.readline())
que = deque()
for _ in range(s):       
  b = sys.stdin.readline().split()
  if b[0] == 'push':
        que.append(b[1])
  elif b[0] == 'pop':
      if not que:
        print(-1)
      else:
        print(que.popleft())
  elif b[0] == 'size':
        print(len(que))
  elif b[0] == 'empty':
      if que:
          print(0)
      else:
          print(1)
  elif b[0] == 'front':
      if not que:
          print(-1)
      else:
          print(que[0])
  elif b[0] == 'back':
      if not que:
          print(-1)
      else:
          print(que[-1])      