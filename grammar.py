# 리스트 컴프리헨션 List Comprehension
# 리스트 컴프리헨션 - 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문.
# ex) 10까지의 숫자가 홀수인 경우, 2를 곱해 출력하라는 리스트 컴프리헨션
a = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(a)
# 풀어서 쓰면
aa = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        aa.append(n * 2)
print(aa)


# 제너레이터 Generator
# 루프의 반복 동작을 제어할 수 있는 루틴 형태
# yeild 구문을 사용하면 제너레이터를 리턴한다. 이 때, 함수는 종료되지 않고 계속해서 끝에 도달할 때 까지 실행된다.
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


def generator():
    yield 1
    yield 2
    yield 'happy'
    yield True
    yield False


g1 = get_natural_number()
g2 = generator()

# 5번만큼 계속 반환
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

# 레인지 Range
# 제너레이터 방식을 활용하는 대표적 함수.
# 주로 for문에서 쓰임.
# for문 대신에 엄청 많은 수의 변수를 생성할 때, range를 통해서 미리 생성해두면
# 메모리 점유율이 훨씬 적다.

list(range(5))
range(0, 5)
type(range(5))

for o in generator():
    print(o, "oh!!!")

for i in range(5):
    print('forIterateRange5')

# 열거형(Enumerate)
# 순서가 잇는 자료형들(리스트, 셋, 튜플 등)을 인덱스를 포함한 enumerate 객체로 리턴.
# 예) a = [1, 5, 'happy', 8, False] 을 list(enumerate(a)) 함수를 통해 출력하면
# [(0, 1), (1, 5), (2, 'happy), (3, 8), (4, False)
a = [1, 5, 'happy', 8, False]
print(list(enumerate(a)))

for i, v in enumerate(a):
    print(i, v)

# 다음의 과정을 for 문으로 쓰려면
for i in range(len(a)):
    print(i, a[i])

# range를 쓰지 않고
i1 = 0
for v in a:
    print(i1, v)
    i1 += 1

