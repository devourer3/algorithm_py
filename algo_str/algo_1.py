# 유효현 팰린드롬
# https://leetcode.com/problems/valid-palindrome/
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
import collections
import re
from typing import Deque

st = "A man, a plan, a canal: Panama"


# class Solution:

# 리스트로 변환한 방법
def isPalindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # isalnum() : 문자나 숫자라면 TRUE
            strs.append(char.lower())
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


# 데크 자료형을 이용
def isPalindrome2(s: str) -> bool:
    # 자료형 데크 선언
    strs: Deque = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# 문자열 슬라이싱을 이용한 방법
def isPalindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)  # re.sub('패턴', '바꿀문자열', '원문자열', 바꿀횟수)
    return s == s[::-1]


isPalindrome1(st)
isPalindrome2(st)
isPalindrome3(st)
