# 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
def solution(my_string):
    answer = ""
    set_string = set(my_string)
    for i in my_string:
        if len(set_string) == 0:
            break
        if i in set_string:
            answer += i
            set_string.remove(i)
    return answer