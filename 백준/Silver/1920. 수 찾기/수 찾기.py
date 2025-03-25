N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for i in B:
    First, Last = 0, N-1
    Find = False

    while First <= Last:
        Mid = (First + Last)//2
        if i == A[Mid]:
              Find = True
              print(1)
              break
        elif i > A[Mid]:
             First = Mid + 1
        else:
             Last = Mid - 1
    
    if not Find:
         print(0)