# 조건에 맞게 수열 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181835

def solution(arr, k):
    return [i + k if k%2 == 0 else i * k for i in arr]