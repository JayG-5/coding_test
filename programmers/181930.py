# 주사위게임 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181930

def solution(a, b, c):
    return eval("*".join([str(sum([a**i,b**i,c**i])) for i in range(1,5-len(set([a,b,c])))]))