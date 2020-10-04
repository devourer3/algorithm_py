# 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수있는 3개의 엘리먼트들을 출력하라.
# https://leetcode.com/problems/3sum/
import time
from typing import List, Tuple

nums = [0, 0, -1, 0, 1, 2, -1, 0, -4, 0]
# nums = [-4, -1, -1, 0, 1, 2]


# 1. 숫자가 작은 순으로 정렬
# 2. 하나의 축(i)을 기준으로 두고, n-2 만큼 반복
# 3.
def threeSum(nums: List[int]) -> List[Tuple[int, int, int]]:
    start = time.time()
    results = []
    nums.sort()
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            print("nums[i]: {}, nums[i-1]: {}".format(nums[i], nums[i - 1]))
            continue
        # 간격을 좁혀가며 합 sum 계산
        left = i + 1
        right = len(nums) - 1
        while left < right:  # 투 포인터 계산
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 인 경우이므로 정답을 튜플에 넣고, 스킵처리
                results.append((nums[i], nums[left], nums[right]))
                # continue
                while left < right and nums[left] == nums[left + 1]:  # 혹시나 left의 같은 숫자들이 존재한다면, 다 results에 넣어야 하기 때문
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # 혹시나 right의 같은 숫자들이 존재한다면, 다 results에 넣어야 하기 때문
                    right -= 1
                left += 1
                right -= 1
    end = time.time()
    print("EX_TIME: {}초".format((end - start) * 1000))
    return results


print(threeSum(nums))
