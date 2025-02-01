from collections import deque
def solution(priorities, location):
    answer = 0
    a = deque([(j, i) for i, j in enumerate(priorities)])

    while a:
      b =  a.popleft()

      if any(b[0] < k[0] for k in a):
         a.append(b)
 
      else :
            answer += 1
            if b[1] == location:
                return answer

    return answer