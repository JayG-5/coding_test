# 피자 나눠먹기(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    return n//7 + int(bool(n%7))