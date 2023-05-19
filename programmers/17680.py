# [1차] 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    cache = deque([''] * cacheSize, maxlen = cacheSize)
    answer = 0
    
    for i in cities:
        i = i.lower()
        answer += 5
        if i in cache:
            answer -= 4
            cache.remove(i)
        cache.append(i)
        
    return answer