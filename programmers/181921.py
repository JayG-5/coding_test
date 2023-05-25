# 배열만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    b_list = list(filter(lambda x: l<=x<=r,[int(bin(i)[2:].replace("1","5")) for i in range((r+1)//5)]))
    return [-1] if not len(b_list) else b_list