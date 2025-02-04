import sys
s = int(sys.stdin.readline())
stack = []
for _ in range(s):       
  b = sys.stdin.readline().split()
  if b[0] == '1':
        stack.append(b[1])
  elif b[0] == '2':
      if not stack:
        print(-1)
      else:
        print(stack.pop())
  elif b[0] == '3':
        print(len(stack))
  elif b[0] == '4':
      if stack:
          print(0)
      else:
          print(1)
  elif b[0] == '5':
      if not stack:
          print(-1)
      else:
          print(stack[-1])