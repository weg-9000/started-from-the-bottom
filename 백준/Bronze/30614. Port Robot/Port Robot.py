stack = []
N = int(input())
a = input()
for i in range(N):
    if a[i].islower():
        stack.append(a[i])

    else:
        if not stack or stack[-1] != a[i].lower():
          print(0)
          break
        else:
          stack.pop()
else:
  if stack:
      print(0)
  else:
      print(1)
    