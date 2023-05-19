# 귤고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    c = 0
    for i,j in enumerate(sorted(Counter(tangerine).values(),reverse = True),1):
        c += j
        if c >= k :
            return i