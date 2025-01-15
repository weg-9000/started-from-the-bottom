def solution(answers):
    patterns = [[1,2,3,4,5] ,[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    score = [0]*3
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                score[j] += 1
 
    max_score = max(score)
    h_score = []
    for i, score in enumerate(score):
        if score == max_score:
            h_score.append(i+1)
    return h_score
solution([1,2,3,4,5])     
     