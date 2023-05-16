# 영어가 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120894


import re

def solution(numbers):
    mapping = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    p = re.compile('|'.join(mapping.keys()))
    return int(p.sub(lambda x: mapping[x.group()], numbers))