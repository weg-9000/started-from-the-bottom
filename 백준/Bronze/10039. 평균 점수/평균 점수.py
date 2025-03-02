a = 0
for _ in range(5):
    b = int(input())
    if b >= 40:
      a += b
    else:
       a += 40
print(int(a/5))