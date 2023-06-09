# 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    return int(sum(num_list)**2 > eval("*".join(map(str,num_list))))