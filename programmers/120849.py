# 모음 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849


import re

def solution(my_string):
    return re.sub(r'[aeiou]','',my_string)