def solution(progresses, speeds):
    d = []
    answer = []
    c=0
    for i in range(len(progresses)):
        a = (100-progresses[i])//speeds[i]
        b = (100-progresses[i])%speeds[i]
        if b > 0:
            d.append(a + 1)
        else:
            d.append(a)
    e = [d[0]]
    for i in d:
        if e[-1:] >= [i]:
            c += 1
        else:
            answer.append(c)
            c = 0
            c += 1
            e.append(i)

    answer.append(c)

    return answer