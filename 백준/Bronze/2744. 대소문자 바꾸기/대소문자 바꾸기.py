N = input()
for i in N:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i, end='')