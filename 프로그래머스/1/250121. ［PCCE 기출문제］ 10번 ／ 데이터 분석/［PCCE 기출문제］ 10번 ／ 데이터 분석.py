def solution(data, ext, val_ext, sort_by):
    ext_dic = {"code":0, "date":1, "maximum":2, "remain":3 }
    data = sorted(data, key = lambda x : x[ext_dic[sort_by]])
    answer = []
    for i in data:
        if i[ext_dic[ext]] < val_ext:
            answer.append(i)
    return answer