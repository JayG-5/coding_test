# 원하는 문자열찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    return int(pat.lower() in myString.lower())