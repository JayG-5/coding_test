# n보다 커질 때까지 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            break
        answer += i
    return answer