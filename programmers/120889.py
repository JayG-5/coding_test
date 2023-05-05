# 삼각형의 완성조건(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    return 2 if sum(sorted(sides)[:-1]) <= max(sides)else 1