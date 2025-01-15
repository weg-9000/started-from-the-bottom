def solution(lines):
    a = [set(range(min(i), max(i))) for i  in lines]
    return len(a[0] & a[1] | a[0] & a[2] | a[1] & a[2])