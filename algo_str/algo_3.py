# 로그파일 재정렬
# 로그를 재정렬하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자다
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
# https://leetcode.com/problems/reorder-data-in-log-files
from typing import List

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

for log in logs:
    print(log.split())


def func(x: List[str]):
    return x.split()[1:], x.split()[0]


def reOrderLogFiles(elements: List[str]) -> List[str]:
    letters, digits = [], []
    for ele in elements:
        print("LOG: ", ele)
        if ele.split()[1].isdigit():  # 각 배열 요소를 띄어쓰기로 split했을 때, 2 번 째 있는 것이 숫자일 때
            digits.append(ele)
        else:
            letters.append(ele)
    print("letters[0].split()[1:]", letters[0].split()[1:])
    print("letters[1].split()[1:]", letters[1].split()[1:])
    print("letters[2].split()[1:]", letters[2].split()[1:])
    # 식별자를 제외한 문자열 [1:](인덱스 1부터 마지막까지) 을 키로 하며, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록 함.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    # -> 람다 대신 letters.sort(key=func)
    return letters + digits


print(reOrderLogFiles(logs))
