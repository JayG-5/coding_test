# 옹알이 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

import re
def solution(babbling):
    return len([i for i in babbling if not re.sub(r'(aya)|(ye)|(woo)|(ma)','',i)])