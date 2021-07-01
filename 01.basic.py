import keyword

myName = '태용'
myMajer = '도우만들기'

print(myName)
print(myMajer)

myName = 111
myName = True
myName = False
myName = 3.141592653

intro = 'Hello'
print(intro)

intro = '안녕하세요...'
print(intro)

nickname = 'Mr. chil'
nickname

print(keyword.kwlist)
#print(keyword.softkwlist) # v 3.9에서 추가되는 기능 그래서 이 버전은 불가능
# 쓸데없는 띄어쓰기는 오류남

bigint= 12345678987654321
print(bigint / 111111111)

bigfloat = 1.234567890123456789
print(bigfloat)

a = 123
b = '456'

a = a + 1
b = b + 1

print(type('123'))
print(type(123))
print(type(False))

# 다중 선언 / 밑에거는 다 같은 경우인듯
x=1
y=1
z=1

x = y = z = 11

# 자릿수구분
million = 1000000
million = 100_0000

# 논리값 확인 : bool / 0이면 false / 그 이외 숫자는 true
bool(True)
bool(1)
bool(100)
bool(-123)
bool(0)

# 자료형 변환
str(123)
int('456')
float('3.141592')


name = input('이름을 입력해주세요\n')
print(name)

# 이름, 국어, 영어, 수학을 입력받아 출력하는 프로그램을 작성
name = input('당신의 이름은?\n')
kor = input('당신의 국어 성적은?\n')
eng = input('당신의 영어 성적은?\n')
mat = input('당신의 수학 성적은?\n')
tot = int(kor) + int(eng) + int(mat)
avg = tot / 3
print(name + '님의 국어성적은 ' + kor + '점이고, 영어성적은 '
      + eng + '점이며, 수학성적은 ' + mat + '점입니다.\n' +
      '따라서 당신의 총점은 ' + str(tot) + '점이고, 평균점수는 ' + str(round(avg, 1))
      + '입니닷!')




