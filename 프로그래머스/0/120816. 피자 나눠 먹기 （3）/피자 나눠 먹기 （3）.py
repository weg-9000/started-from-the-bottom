def solution(slice, N):
    a = N//slice
    if N%slice != 0:
        a += 1
    return a