# 숨어있는 숫자의 덧셈 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120864

import re
def solution(my_string):
    return sum(map(int,re.sub(r'[a-zA-Z]',r' ',my_string).split()))