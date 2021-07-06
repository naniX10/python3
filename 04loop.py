# 반복문
# 1 ~ 10 까지 정수 출력
for i in range(1,10 + 1):
    print(i)

# 2 ~ 10 사이 짝수 출력
for i in range(2, 10+1, 2):
    # print(i)
    print(i, end=' ')

# for i in range(1, 10+1):
#     if i % 2 == 0:
#         print(i)

# 입력 횟수멘치 출력
num = int(input('메일 발송 횟수를 입력하세요 '))
for i in range(1, num + 1):
    print('메일발송!')

# 1 ~ 10 까지 정수 출력! 3의 배수는 <3의배수!> 라고 출력
for i in range(1, 10+1):
    if (i % 3 == 0):
        print(f'num = {i}')
        print('3의 배수!')
    else:
        print(f'num = {i}')

# 구구단 출력
num = int(input('1 부터 9 사이의 숫자를 입력해주세요'))
for i in range(1, 9+1):
    print(f'{num} × {i} = {num * i}')

# 1 ~ 10 까지의 합
sum = 0
for i in range(1, 10+1):
    sum += i # sum = sum + i
print(sum)

# 3과 7의 공배수, 최소공배수
for i in range(1, 100+1):
    if (i % 3 == 0 and i % 7 == 0):
        print(i)

min = 100
print('3과 7의 공배수', end= ' ')
for i in range(100, 1, -1):
    if (i % 3 == 0 and i % 7 == 0):
        if min >= i: min = i
        print(i, end=', ')
print(f'최소공배수 {min}')


for i in range (-10,1,1):
    print(i, end=' ')

# 1 ~ 10 까지 출력
for i in range(10):
    print (i+1)

# 반복문에 range 대신 문자열 사용
for c in 'hoooooooo':
    print(c, end=', ')
print()

# 50 보다 작은 7의 배수
for i in range(7, 50+1, 7):
    print(i)

for i in range(50):
    if i % 7 == 0: print(i, end=' ')
print()

# 1 ~ 10 까지 출력
i = 1
while i <= 10:
    print(i)
    i += 1

# 1 ~ 30 에서 홀 짝을 구분해서 출력하기
i = 1
while i <= 30:
    if i % 2 == 0:
        print(f'짝수 : {i}')
    else:
        print(f'홀수 : {i}')
    i += 1

# 구구단 3 단 출력
num = int(input('1 ~ 9 사이의 숫자를 하나 입력하세요 '))
i = 1
while i <= 10:
    print(f'{num} x {i} = {num*i} ')
    i += 1

# 0 ~ 100 사이 정수중 3 과 8의 공배수와 최소 공배수 출력
i = 1
min = 100
while i <= 100:
    if (i % 3 == 0 and i % 8 == 0):
        print(f'공배수 : {i}')
        if min > i:
            min = i
    i += 1
print(f'최소공배수 : {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1. 진행,  2. 종료 '))
    if (code == 1):
        print('게임 진행')
    else:
        flag = False
        print('게임 종료')

# 1 ~ 50 까지 정수 중 3의 배수를 더하기?
sum = 0
for i in range(1, 50+1):
    if (i % 3 != 0): continue
    sum += i
print(sum)

sum = 0
for i in range(1, 50+1):
    if (i % 3 == 0):
        sum += i
print(sum)

# 1 ~ 100 까지 모든 정수 더하기
# 단, 정수의 합이 500이 넘었을때의 정수는 무엇인가???
sum = 0
for i in range(1, 100+1):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# for - else
# 1 ~ 10 까지의 정수의 총합을 구하고 반복이 끝나는 경우 완료 메세지 출력
sum = 0
for i in range(10): # 0 ~ 9 까지라서 밑에서 1 더해주는 듯
    sum += (i + 1)
else:
    print(f'총합 : {sum} / 계산 완료!')

# 삼각형 넓이?
mul = 0
ga = 1
se = 1
i = 1
while mul <= 150:
    ga = 2 * i
    se = 3 * i
    mul = ga * se / 2
    i += 1
    if (mul > 150):
        break
    print(f'삼각형 넓이 : {mul}, 가로 길이 : {ga}, 세로 길이 : {se} ')

wid = 2
hei = 3
area = 0
while area <= 150:
    area = wid * hei / 2
    print(area, hei, wid)
    wid += 2
    hei += 3

# 1 ~ 100까지 숫자 중 5와 7의 배수를 빼고 출력하기
for i in range (1, 100+1):
    if (i % 5 == 0 or i % 7 == 0):
        pass
    else:
        print(i)

for i in range (1, 100+1):
    if (i % 5 == 0 or i % 7 == 0):
        continue
    print(i, end=', ')
print()


#
num = 0
while True:
    if (num == 30): break
    print(num)
    num += 1

for num in range(30):
    print(num)

# 중첩 반복문으로 구구단 출력?
for i in range(1, 19+1):
    for j in range(2, 19+1):
        print(f'{j:2d} x {i:2d} = {j * i:2d} \t', end=' ')
    print()
print()



