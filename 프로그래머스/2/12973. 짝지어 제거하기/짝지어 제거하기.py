def solution(s):
    b = []
    for i in s:
        if b and b[-1] == i:
            b.pop()
        else:
            b.append(i)
    return(int(not b) )

