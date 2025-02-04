import sys
s = int(sys.stdin.readline())
stack = []
for _ in range(s):       
  b = sys.stdin.readline().split()
  if b[0] == 'push':
        stack.append(b[1])
  elif b[0] == 'pop':
      if not stack:
        print(-1)
      else:
        print(stack.pop())
  elif b[0] == 'size':
        print(len(stack))
  elif b[0] == 'empty':
      if stack:
          print(0)
      else:
          print(1)
  elif b[0] == 'top':
      if not stack:
          print(-1)
      else:
          print(stack[-1])

