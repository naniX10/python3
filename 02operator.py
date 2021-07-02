# num1 = 10
# num2 = 11
# num3 = num1 + num2 # 정수 + 정수 = 정수
#
# num1 = 10.5
# num2 = 39.5
# num3 = num1 + num2 # 실수 + 실수 = 실수
#
# num1 = 10
# num2 = 39.5
# num3 = num1 + num2 # 실수 + 정수 = 실수
#
# # 매출액 구하기
# jan = input('1월 매출을 입력해주세요')
# feb = input('2월 매출을 입력해주세요')
# mar = input('3월 매출을 입력해주세요')
# one = int(jan) + int(feb) + int(mar)
# print('1분기 전체 매출 : ' + str(one) + ' 원')
#
# num1 = 3.14
# num2 = 0.85
# num3 = num1 + num2
# print(num3)
# float(num3)
# int(num3)
#
# # 순이익 구하기
# inp = input('1분기 매출 : ')
# out = input('1분기 지출 : ')
# ben = int(inp) - int(out)
# print ('수익 : ' + str(ben) + '원')
#
# # 넓이 구하기
# long = int(input('가로 길이 : '))
# let = int(input('세로 길이 : '))
# room = long * let
# print('방 넓이 : {0} m²'.format(room))
#
# str1 = 'Helloworld!'
# str1 * 3
# str1 * -2
#
# # BMI 구하기
# kg = int(input('몸무게(kg) : '))
# m = float(input('신장(m) : '))
# bmi = kg / (m*m)
# print('BMI : {0:.1f}'.format(bmi))
# print(f'BMI : {bmi:.1f}') # f-string : 파이썬 3.6부터 지원
#
# #print 출력 속도 : .format > % > f-string
#
#
# # 동전 홀짝?
# coin = int(input('동전의 개수는?'))
#
# isEven = coin % 2
# print(f'동전의 홀짝은? (0:짝 1:홀) {isEven}')
#
# # // 하면 정수부분만 보임
# 10 / 3
# 10 // 3
#
# # 빵 나눠주기 / 빵, 나눠줄 빵개수 입력 / 최대몇명까지 가능? 남는 개수는?
# allbr = int(input('빵의 총 개수는?'))
# disdr = int(input('나눠줄 빵의 개수는?'))
# stu = allbr // disdr
# nam = allbr % disdr
# print(f'빵의 총 개수 : {allbr}')
# print(f'빵을 몇개씩 나눠 주는가 : {disdr}')
# print(f'빵을 나누어 줄 수 있는 학생 수 : {stu}')
# print(f'남는 빵 개수 : {nam}')
#
# # 거듭제곱
# 2 ** 2 # 2 X 2
# 2 ** 4 # 2 X 2 X 2 X 2
# 2 ** 10 # 2 X 2 X 2 X 2 X 2 X 2 X 2 X 2 X 2 X 2
#
# day = int(input('경과한 날짜는?'))
# die = 2 ** day
# print(f'감염자의 수 : {die}')
#
# 복리 계산? / 원금, 유치기간, 연이율을 입력받아 복리 계산후 총 수령액 출력
# 1년차 원금 * 이율 = 원금
# 2년차 원금 * 이율 = 원금
# ...
# 5년차 원금 * 이율 = 원금
money = 500_0000
dur = 5
inter = 5.0
takes = money + (money * 0.05) # 1년
# takes = takes + (takes * 0.05) # 2년
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 3년
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 4년
takes += takes * 0.05
# takes = takes + (takes * 0.05) # 5년
takes += takes * 0.05
#
# # 키 판정?
# cm = int(input('당신의 키는? (cm)'))
# ride = 120 <= cm
# print(f'탑승 가능 여부 : {ride} (True: 탑승가능/ False: 탑승불가)')
#
# # 키 판정
# cm = int(input('당신의 키는? (cm)'))
# # ride = (120 <= cm) and (cm <= 170)
# ride = 120 <= cm < 170
# print(f'탑승 가능 여부 : {ride} (True: 탑승가능/ False: 탑승불가)')
#
# # short circuit evaluation
#
# num1 = 17
# num2 = 20
# (num1 < 15) and (num2 > 15) #False and True
#
# num1 = 10
# num2 = 20
# (num1 < 15) or (num2 < 15) #True and False
#
# # (num1 < 5) and qwe # 파이썬 3.8 에서만
#
# # 삼항 연산자
# # 참일때 값 if 조건식 else 거짓일때 값
# num = 10
# '짝수' if (num % 2 == 0) else '홀수'

# 적자 흑자 판단하기
inp = int(input('매출액은?'))
out = int(input('지출액은?'))
sum = inp - out
lol = '흑자' if (sum >= 0) else '적자'
print(f'현재 {sum} 원 {lol} 상태입니다')

# 윤년 여부 알아보기?
# 4 로 나눠 떨어지고 100으로 나눠 떨어지지 않음
# 400 으로 나눠 떨어짐
iny = int(input('알아보고 싶은 년도는?'))
leap = (((iny % 100) != 0 and (iny % 4) == 0) or (iny % 400) == 0)
what = '윤년입니다' if (leap) else '윤년이 아닙니다'
print(f'입력해주신 {iny}년은 {what}')

