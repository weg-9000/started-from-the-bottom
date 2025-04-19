T, S = map(int, input().split())

if S == 0:
    if T <= 11:
        print("280")
    elif T>=11 and T <= 16:
        print("320")
    else:
        print("280")
elif S == 1:
    print("280")