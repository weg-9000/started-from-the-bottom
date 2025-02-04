N = int(input())
for i in range(N):
  stack = []
  s = str(input())
  for c in s:
      if c == "(" :
            stack.append(c)
      elif c == ")":          
          if not stack:
            print('NO')
            break
          else:
            stack.pop()
  else:
    if stack:
        print('NO')
    else:
        print('YES')