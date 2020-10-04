# 거스름돈
# 당신은 음식점의 계산을 도와주는 점원이다.
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정.
# 손님에게 거슬러 줘야 할 돈이 N원 일때, 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

from typing import List

n = 1540
curr = [500, 100, 50, 10]


# 1. 1540원을, 주어진 동전에서 최소 개수만큼 구하려면
# 2. 값이 제일 큰 순으로 나누어 나간다.
def exchange(money: int, curr: List[int]) -> int:
    count = 0

    for coin in curr:
        count += money // coin  # 해당 화폐로 거슬러 줄 수 있는 동전 최대값의 동전의 개수
        money %= coin  # money 는, 동전 최대값으로 나눈 나머지 만큼으로 변환
    return count


print(exchange(n, curr))