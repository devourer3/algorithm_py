# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며 ,구두점(마침표, 쉼표 등) 또한 무시한다.
# https://leetcode.com/problems/most-common-word
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 리스트 컴프리헨션
# paragraph에서 단어가 아닌 것은 없애고, 공백을 매개로 나누고, banned에 들어가지 않은 단어들을 words 리스트에 append 함
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

counts = collections.Counter(words)

# 흔하게 노출되는 단어 순으로 정렬
print(counts.most_common(10))
# 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
print(counts.most_common(1)[0][0])

