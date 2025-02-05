import sys
N = int(sys.stdin.readline())
stack = []
stack2 = []
b = 0
for _ in range(N):
    stack.append(int(sys.stdin.readline()))
for i in stack[::-1]:
    if stack2[-1:] < [i]:
        b += 1
        stack2.append(i)
print(b)