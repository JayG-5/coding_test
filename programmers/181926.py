# 수 조작하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181926

def solution(n, control):
    return eval(str(n)+control.replace("w","+1").replace("s","-1").replace("d","+10").replace("a","-10"))