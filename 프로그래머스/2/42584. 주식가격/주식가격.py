def solution(s):
    p = [0]
    answer = [0]*len(s)
    for i in range(1, len(s)):
        while p and s[i] < s[p[-1]]:
            j = p.pop()
            answer[j] = i - j
        p.append(i)
    while p:
        j = p.pop()
        answer[j] = len(s) -1 - j
    return answer

        