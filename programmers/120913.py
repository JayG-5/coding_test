# 잘라서 배열로 저장하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120913

import re
def solution(my_str, n):
    return re.findall(r'.{1,%d}'%n,my_str)