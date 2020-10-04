#  숫자 카드 게임
#  규칙1. 행(N), 열(M) 로 이루어진 카드 들 중, 한 행을 선택한다
#  규칙2. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
#  따라서, 카드들 중 행에 가장 낮은 값이 그나마 큰 값인 행을 선택해야 함.

#  카드들이 N * M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만들라.

def cardSpread():
    n, m = map(int, input("n, m 행렬을 공백을 기준으로 입력 해 주세요: ").split())

    result = 0
    # 한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int, input("{}행의 카드들을 공백을 기준으로 입력 해 주세요.".format(i)).split()))
        # 현재 줄에서 '가장 적은 수' 찾기
        min_value = min(data)
        # '가장 적은 수'들 중에서 가장 큰 수 찾기
        result = max(result, min_value)
    print(result)


cardSpread()