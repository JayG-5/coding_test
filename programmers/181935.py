# 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935

def solution(n):
    return sum(i**2 for i in range(0,n+1,2)) if n % 2 == 0 else sum([i for i in range(1,n+1,2)])