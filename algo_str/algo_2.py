# 문자열 뒤집기
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
# https://leetcode.com/problems/reverse-string
from typing import List

st = ["h", "e", "l", "l", "o"]


# class Solution:

def reverseString(s: List[str]) -> None:
    s.reverse()
    print(s)


# print(reverseString2(st))
# print(st)

st = st[::-1]
print(st)

# st = st[::-1]
# print(st)
