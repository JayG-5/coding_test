# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    count = 0
    while people:
        count += 1
        boat = people.pop()
        if not people:
            break
        if boat + people[0] <= limit:
            people.popleft()
            continue
    return count