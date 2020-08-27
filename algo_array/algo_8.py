# 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
# > left, right 모두 중앙으로 1만큼 계속 이동하면서, 현재 높이가 이전 높이보다 작을 때만, volume을 채움.
# https://leetcode.com/problems/trapping-rain-water/
from typing import List

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 0]


# 투 포인터 방법
# 1. 왼쪽에서 오른쪽으로 포인터가 계속 이동
# 2. 현재 포인터의 높이가, 이전의 높이보다 n만큼 작을경우, volume에 n만큼 더함.
# 3.
def rainTrap(height: List[int]) -> int:
    # if not height:
    #     return 0

    volume = 0  # 빗물이 저장될 수 있는 부피들의 총 합
    left = 0  # 가변하는 왼쪽 좌표 (0)
    right = len(height) - 1  # 오른쪽 좌표 (11)
    left_max = height[left]  # 왼쪽 좌표 중 가장 높은 높이 값(처음은 0)
    right_max = height[right]  # 오른쪽 좌표 중 가장 높은 높이 값(처음은 1)

    # 왼쪽 좌표가 오른쪽 좌표가 크거나 같을 때까지
    while left < right:
        left_max = max(height[left], left_max)  # 현재 왼쪽 포인터의 높이 값이, 이전 왼쪽 최대 높이보다 높을 때 교체
        right_max = max(height[right], right_max)  # 현재 오른쪽 포인터의 높이 값이, 이전 오른쪽 최대 높이보다 높을 때 교체

        # 왼쪽의 좌표의 현재까지 가장 높은 높이와 오른쪽 현재까지 가장 높은 높이의 비교 후,
        # 더 높은 쪽을 향해 각각의 포인터가 이동
        if left_max <= right_max:  # 왼쪽의 최대 높이 값이 오른쪽의 최대 높이값보다 작거나 같을 때,
            volume += (left_max - height[left])  # 25# 에서, 이번 높이가 이전 높이보다 낮은 경우, 그 값만큼 volume에 더함
            left += 1  # 왼쪽 포인터는 오른쪽으로 한 번 이동
        else:  # 왼쪽의 최대 높이 값이 오른쪽의 최대 높이값보다 클 때,
            volume += (right_max - height[right])  # 26# 에서, 이번 높이가 이전 높이보다 낮은 경우, 그 값만큼 volume에 더함
            right -= 1  # 오른쪽 포인터는 왼쪽으로 한 번 이동
    return volume  # 왼쪽 좌표가 오른쪽 좌표보다 클 때, 총 물의 높이의 값


# 스택 방법
def stackRainTrap(height: List[int]) -> int:
    stack = []
    volume = 0

    # 좌표들 순회
    for i in range(len(height)):
        # 변곡점(현재 높이가 이전 높이보다 높을 때)을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()
            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters
        stack.append(i)
    return volume


print(rainTrap(heights))
print(stackRainTrap(heights))
