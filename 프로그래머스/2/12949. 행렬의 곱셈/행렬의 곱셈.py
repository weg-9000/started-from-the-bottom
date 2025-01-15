def solution(arr1, arr2):
    r0, c0 = len(arr1), len(arr1[0])
    r1, c1 = len(arr2), len(arr2[0])
    answer = [[0]*c1 for _ in range(r0)]
    for i in range(r0):
        for j in range(c1):
            for k in range(c0):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    return answer