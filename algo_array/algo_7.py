# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# https://leetcode.com/problems/two-sum
from typing import List, Tuple

nums = [13, -20, 0, 19, -7, 2, 3, 5, 10, 7, 11, 15]

target = 9


# 브루트 포스로 계산
# 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식
# 시간 복잡도는 O² 로, 매우 느림(5000 밀리 초)
def useBFSTwoSum(nums: List[int], target: int) -> Tuple[int, int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


# in을 이용한 탐색 방법
# 모든 조합을 비교하지 않고, 타깃에서 첫 번째 값을 뺀 (target - n) 이 존재하는지 탐색
# enumerate는 자바의 HashSet과 같다
# 시간 복잡도는 in(28#) 에서 O(n) 으로, 전체 시간 복잡도는 O² 이다.
# 하지만, in 연산쪽이 훨씬 빠름 (8 ~ 900 밀리 초)
def useInTwoSum(nums: List[int], target: int) -> Tuple[int, int]:
    for i, n in enumerate(nums):  # [(0, 13), (1, -20), (2, 0), (3, 19), (4, -7) ... ]
        complement = target - n  # complement는 타깃에서 i 번째의 value를 뺀 값(보수)
        if complement in nums[i + 1:]:  # complement 값이 i+1 부터의 정렬된 값에 존재하면,  in은 자바의 contains와 같음.
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


# 첫 번째 수를 뺀 결과 - 딕셔너리를 이용하여 키 조회
# 타겟에서 첫 번째 수를 빼면, 두 번째 수를 바로 알아낼 수 있다.
# 분할 상환 분석에 따른 시간 복잡도는 O(1) 이며, 전체는 O(n)이다. (48밀리초)
def useDicTwoSum(nums: List[int], target: int) -> Tuple[int, int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    # nums_map: {13: 0, -20: 1, 0: 2, 19: 3, -7: 4, 2: 5, 3: 6, 5: 7, 10: 8, 7: 9, 11: 10, 15: 11}
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]


# 조회구조 개선
def useAdvDicTwoSum(nums: List[int], target: int) -> Tuple[int, int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
        if target - num in nums_map:
            return nums_map[target - num], i


# print("useBFSTwoSum: ", useBFSTwoSum(nums, target))

# print("useInTwoSum: ", useInTwoSum(nums, target))

# print("useDicTwoSum: ", useDicTwoSum(nums, target))

print("useAdvDicTwoSum: ", useAdvDicTwoSum(nums, target))
