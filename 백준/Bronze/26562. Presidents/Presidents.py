dict = {"Franklin": 100, 'Grant':50, 'Jackson':20, 'Hamilton':10, 'Lincoln':5, 'Washington':1}
N = int(input())
b = 0
for i in range(N):
    a = input().split()
    for j in a:
        b += dict[j]
    print(f'${b}')
    b = 0