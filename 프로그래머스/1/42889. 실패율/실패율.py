def solution(N, stages):
    answer = []
    lent = len(stages)
    for i in range(1, N+1):
        counts = stages.count(i)
        if lent == 0:
            fail = 0
        else:
            fail = counts / lent #실패율
        answer.append((i, fail)) # 스테이지 번호와 실패율을 튜플로 묶어준다.
        lent -= counts # 실패율을 계산하기 위해 실패한 플레이어 수를 빼준다.
    answer = sorted(answer, key=lambda x: -x[1]) # 실패율을 기준으로 내림차순 정렬
    answer = [i[0] for i in answer] # 스테이지 번호만 리스트에 담아준다.
    return answer