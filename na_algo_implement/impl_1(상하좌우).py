# 상하좌우 (110 p)
# 여행가 A는 N * N 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1) 이며, 가장 오른쪽 아래 좌표는 (N, N) 에 해당한다.
# 여행가 A는 상(U), 하(D), 좌(L), 우(R) 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1) 이다.

def upDownLeftRight():
    # N을 입력받기
    n = int(input("N 값을 입력하시오."))
    x, y = 1, 1
    plans = input("공백을 구분으로 둬, N개를 입력하시오.").split()

    # L, R, U, D에 따른 이동 방향
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

    print(x, y)


upDownLeftRight()
