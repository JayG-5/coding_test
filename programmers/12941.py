# 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    return sum(map(lambda x:x[0]*x[1],zip(sorted(A),sorted(B)[::-1])))