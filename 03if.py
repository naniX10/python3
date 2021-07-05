# if문
num = int(input('숫자를 하나 입력하세요 '))
if (num > 10):
    print(f'{num}은 10보다 작지 않았습니다!')
else:
    print(f'{num}은 10보다 크지 않았습니다!')

# 대충 속도위반?
speed = int(input('현재 속도는? '))
if (speed > 50):
    print('속도 위반!!!')
# if (speed > 50) : print('속도 위반!!!')  도 가능

# 합격 불합격 출력
score = int(input('당신의 점수를 입력해주세요! '))
if (score >= 80):
    print('합격을 축하드립니다!!!!!!!!!!!!!')
else:
    print('아쉽습니다. 다음 기회를 노려보세요')

# 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 작성 가능
# score = int(input('당신의 점수를 입력해주세요! '))
# if (score >= 80):
#     pass
# else:
#     pass

temp = int(input('기계 온도를 입력하세요! '))
if (temp >= 40):
    print('팬(Fan) 가동!')
else:
    print('팬(Fan) 중지')

# 입력받은 숫자를 3으로 나눠 소수점 첫째 자리에서 반올림

num = int(input('숫자를 하나 입력해주세요! '))

res = num / 3
if (res - int(res) >= 0.5):
    res = int(res) + 1 # 소수이하 버리고 올림
else:
    res = int(res) # 소수이하 버림
print(f'결과 : {res}')

# 마일리지
mile = int(input('현재 적립된 마일리지를 입력해주세요 '))
if (mile >= 1000):
    print('마일리지 사용 가능하십니다!')
else:
    print('마일리지 사용을 하실수 없습니다, 1000 마일리지까지 적립 후 이용 가능합니다 ')

# 성적처리
score = int(input('점수를 입력해주세요 '))
if (70 > score >= 60):
    print('양')
elif (80 > score >= 70):
    print('미')
elif (90 > score >= 80):
    print('우')
elif (100 >= score >= 90):
    print('수')
else:
    print('가')

# 대충 주문 시스템
order = int(input('안녕하세요! 만나서 반갑습니다!\n'
                  '어느 나라에서 오셨나요?\n'
                  '번호를 선택해 주세요!\n'
                  '1. 대한민국 2.USA 3.中國 '))
if (order == 1):
    print('주문하시겠습니까?')
elif (order == 2):
    print('Would you like to order?')
elif (order == 3):
    print('您要点菜吗？')
else:
    print('Would you like to order?')

# 대충 재난지원금
people = int(input('가구 인원수를 입력해주세요 '))
# if (people == 1):
#     print('40,0000원 지원')
# elif (people == 2):
#     print('60,0000원 지원')
# elif (people == 3):
#     print('80,0000원 지원')
# elif (people >= 4):
#     print('100,0000원 지원')
if (people == 1):
    money = 40_0000
elif (people == 2):
    money = 60_0000
elif (people == 3):
    money = 80_0000
else:
    money = 100_0000
print(f'{money:,}원 지원')

# BMI
# bmi = int(input('BMI 지수를 입력해주세요!'))
# if (bmi <= 90):
#     print('저체중')
# elif (110 >= bmi > 90 ):
#     print('정상 체중')
# elif (120 >= bmi > 110 ):
#     print('과체중')
# elif (140 >= bmi > 120 ):
#     print('비만')
# else:
#     print('고도비만')
cm = int(input('키는?'))
kg = int(input('몸무게는?'))
cm = cm - 100
bmi = kg / (cm * cm)

if bmi > 30: print('고도비만')
elif bmi > 25: print('비만')
elif bmi > 23: print('과체중')
elif bmi > 18.5: print('정상 체중')
else: print('저체중')

# 버스
day = int(input('요일을 선택하세요 (1 ~ 3)\n'
                '1.월 ~ 금  2. 토요일  3. 공휴일 '))
if (day == 2 or day == 3):
    print('토요일 및 공휴일은 단속하지 않습니다')
elif(day == 1):
    print('버스 전용차로 단속 중입니다.')
    bus = int(input('차종을 선택하세요 \n'
              '1. 버스  2. 승용차 '))
    if (bus == 1):
        print('버스입니다 - 단속 대상 아님')
    elif (bus == 2):
        print('버스 전용차로 위반!!!')


# 마스크 판매
age = int(input('만 나이 입력 : '))
if (age >= 65):
    mess = '언제든지'
else:
    endBirthYear = int(input('출생년도 끝자리 입력 : '))
    if (endBirthYear == 1 or endBirthYear == 6):
        mess = '월요일'
    elif (endBirthYear == 2 or endBirthYear == 7):
        mess = '화요일'
    elif (endBirthYear == 2 or endBirthYear == 7):
        mess = '수요일'
    elif (endBirthYear == 4 or endBirthYear == 9):
        mess = '목요일'
    else:
        mess = '금요일'
print(f'{mess} 구매 가능합니다')

