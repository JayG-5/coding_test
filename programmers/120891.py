# 369게임
# https://school.programmers.co.kr/learn/courses/30/lessons/120891

import re
def solution(order):
    return len(re.findall('[369]',str(order)))