# 대소문자 바꿔서 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181949

str = input()
for i in str:
    str = str[1:] + (i.lower() if i.isupper()else i.upper())
print(str)