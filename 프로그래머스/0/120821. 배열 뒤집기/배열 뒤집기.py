def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        k = len(num_list) - (i+1)
        answer.append(num_list[k])
    return answer