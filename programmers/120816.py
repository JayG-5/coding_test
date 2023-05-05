# 피자나눠먹기(3)
# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    return n//slice + int(bool(n%slice))