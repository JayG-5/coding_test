# 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908

def solution(my_string, is_suffix):
    return int(is_suffix in [my_string[i:] for i in range(len(my_string))])