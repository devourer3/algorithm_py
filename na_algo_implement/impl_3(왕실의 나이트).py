# 왕실의 나이트(p. 115)
# 체스판은 a1 b1 c1 d1 ~ h1
#       a2 b2 c2 d2 ~ h2
#       ...
#       a8 b8 c8 d8 ~ h8
# 상하좌우 강화판


def royalKnight():
    # 현재 나이트의 위치 입력받기
    input_data = input("현재 나이트의 좌표를 입력하시오(예. a1):")
    row = int(input_data[1])
    column = int(ord(input_data[0]))

    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]
        # 해당 위치로 이동이 가능하다면 카운트 증가
        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            result += 1

    print(result)


royalKnight()
