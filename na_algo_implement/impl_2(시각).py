# 시각 (113p)
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

def timeSum():
    hour = int(input("구할 시간(0시 ~ 23시) 을 입력하시오: "))
    count = 0
    for h in range(hour + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 '3' 이 포함되어 있다면 카운트 증가
                if '3' in str(h) + str(j) + str(k):
                    count += 1
    print(count)


timeSum()
