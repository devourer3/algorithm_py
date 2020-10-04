# 큰 수의 법칙
# N만큼의 크기를 갖는 특정 배열에서 M만큼 반복되는 수를 더하는 값을 찾는 문제
# 단, K만큼 반복하는 데 제한이 있음
# 예를들어, [2, 4, 6, 7, 10] 의 배열이 있을 때, M이 6이고, K가 2일 경우
# 10 + 10 + 7 + 10 + 10 + 7 이 되는 경우를 뜻 함.

from typing import List


# 그리디 알고리즘은 직접 노트에 써봐서 규칙을 알아가는게 중요.
def greatNumbers():
    # N, M, K 를 공백으로 구분하여 입력받기
    n, m, k = map(int, input("n, m, k 값을 각각 공백을 기준으로 입력 해 주세요(예. 3 4 5): ").split())

    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input("{}개 만큼의 배열을 공백을 기준으로 입력 해 주세요(예. 2 3 5 7 8 10): ".format(n)).split()))

    data.sort()  # 입력받은 수 정렬
    first = data[n - 1]  # 가장 큰 수
    second = data[n - 2]  # 두 번째로 큰 수

    # 가장 큰 수가 더해지는 횟수 계산
    count = m // (k + 1) * k
    print("COUNT: ", count)
    count += m % (k + 1)
    print("COUNT: ", count)

    result = 0
    result += count * first  # 가장 큰 수 더하기
    result += (m - count) * second  # 두 번째로 큰 수 더하기

    print(result)


greatNumbers()
