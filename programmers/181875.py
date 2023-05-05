# 배열에서 문자열 대소문자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181875

# enumerate로 푸는방법이 있음
# enumerate를 쓰면 각 개체가 (index,개체)로 구성된 튜플반환

def solution(strArr):
    return [strArr[i].lower()if i%2 == 0 else strArr[i].upper() for i in range(len(strArr))]