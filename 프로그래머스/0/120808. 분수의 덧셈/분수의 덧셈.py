def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    answer = []
    for i in range(min(a,b), 0 , -1):
        if (a%i == 0) and (b%i == 0):
            answer.append(int(a/i))
            answer.append(int(b/i))
            break
    return answer