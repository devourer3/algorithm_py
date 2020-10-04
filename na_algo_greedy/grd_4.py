# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 다음 두 과정중 하나를 반복적으로 선택항 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어질때만 선택할 수 있다.
# N에서 1을 뺀다. -> N이 K로 나누어 질 때, N을 K로 나눈다.
# N과 K가 주어질 때, N이 1이 될 때까지 1번 혹은 2번 과정을 수행하애 하는 최수 횟수를 구하는 프로그램을 작성하시오.


def minusOrdivideRaw():
    # N이 K이상이면, K로 계속 나누기
    n, k = map(int, input("n과 k를 공백으로 구분하여 입력 해 주세요: ").split())
    result = 0

    # N이 K이상이라면, K로 계속 나누기
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n >= k:
        while n % k != 0:
            n -= 1
            result += 1
            # K로 나누기
        n //= k
        result += 1

    # 마지막으로 남은 수에 대하여 1씩 빼기
    while n > 1:
        n -= 1
        result += 1

    print(result)


def minusOrDivide():
    n, k = map(int, input("n과 k를 공백으로 구분하여 입력 해 주세요: ").split())
    result = 0

    while True:
        # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # K로 나누기
        result += 1
        n //= k
    # 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1)
    print(result)


minusOrdivideRaw()

minusOrDivide()
