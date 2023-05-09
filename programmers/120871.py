# 저주의 숫자 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    d_count = n
    count = 0
    while d_count:
        count += 1
        if count % 3 == 0 or '3' in str(count):
            continue
        d_count -= 1
    return count