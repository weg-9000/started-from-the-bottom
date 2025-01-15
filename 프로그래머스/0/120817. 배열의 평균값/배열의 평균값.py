def solution(numbers):
    a = 0
    for i in numbers:
        a += i
    a = a / len(numbers)
    return a
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])