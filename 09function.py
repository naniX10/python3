# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시 코드가 섞이지 않게
# 하기 위한 목적도 있음 - 모듈

def startSensor():
    print('온도 센서 작동을 시작')

def stopSensor():
    print('온도 센서 작동을 중지')

startSensor()
stopSensor()

# 노트북 파우치
# 1센치 > 0.393701 인치

def convertCM2inch(cm):
    # return cm * 0.393701
    print(f'{cm * 0.393701:.2f}')

cm = int(input('파우치 길이를 입력하세요'))
convertCM2inch(cm)
# print( convertCM2inch(cm) )

# 이동 거리 계산
def computeDistance(time, speed):
    print(f'이동거리는 {time * speed} km 입니다')


time = float(input('이동시간은?'))
speed = float(input('이동속도는?'))
computeDistance(time, speed)

def add():
    print(a + b)

a = input('a는?')
b = input('b는?')

add()





