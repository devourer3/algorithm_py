# 문자열 배열을 받아 애너그램 단위로 그룹핑 하라.
# https://leetcode.com/problems/group-anagrams
import collections

a = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 애너그램 관계인 단어들은 정렬하면, 서로 같은 값을 갖게 된다.
# sorted() 함수는 문자열도 잘 정렬하며, 결과를 리스트 형태로 리턴한다.
# 이를 다시 키로 사용하기 위해 join()으로 합쳐 이 값을 키로 하는 딕셔너리로 구성한다.

anagrams = collections.defaultdict(list) # 존재하지 않는 딕셔너리 KeyError를 방지하기 위해 defaultdict로 생성한다.

for word in a:
    # print("for sorted", sorted(word))
    # 정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)
print(anagrams.values())
