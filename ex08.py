# 차량 2부제
car = int(input('차량번호 4자리를 입력해 주세요'))
# days = int(input('오늘의 날짜를 입력해 주세요'))
from datetime import datetime as days
days.now()
days.today().second


if (days % 2 == 0):
    print('오늘 입차 : 번호가 짝수인 차량')
    if (car % 2 == 0):
        print('귀하의 차량은 입차 가능합니다')
    else:
        print('귀하의 차량은 입차 불가합니다')
else:
    print('오늘 입차 : 번호가 홀수인 차량')
    if (car % 2 != 0):
        print('귀하의 차량은 입차 가능합니다')
    else:
        print('귀하의 차량은 입차 불가합니다')

# eoo = '짝수'
# if (days % 2 != 0): eoo = '홀수'
# print(f'오늘 입차 : 번호가 {eoo}인 차량')
#
# pon = '입차 불가'
# # if (car % 2 == 0 and days % 2 != 0): 검사 2번 실행
# if (car % 2 == 0 and eoo == '짝수'):
#     pon = '입차 가능'
#
# print(f'귀하의 차량은 {pon}합니다')