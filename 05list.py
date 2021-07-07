# 파이썬 리스트?

attendList = ['순철','병헌','민우','찬호','민태']
print(attendList)

numbers = [1,2,3,4,5,6,7]
print(numbers)

complex = [1, 2.0 , 3.1415926, 40, '5', "60"]
print(complex)

for data in numbers:
    print(data)

for data in complex:
    print(data)

len(numbers)
len(complex)

msg = 'Hello, World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print(len(msg))

# 문자열 길이?
msg = input('문장을 입력해주세용')
print(f'입력한 문장의 길이 : {len(msg)}')

print(len(['안녕안녕!!']))
print(len('안녕안녕!!'))

# 리스트의 모든 항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])

for i in range(6):
    print(complex[i])

for item in complex:
    print(item)

# enu~~ 쓰면 순서하고 항목을 출력 가능
for idx, item in enumerate(complex):
    print(f'{idx}, {item}')

print(complex.index(3.1415926))

sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
print(sports.index('soccer'))
print(sports[len(sports)-1])

for idx, item in enumerate(sports):
    print(f'{idx}, {item}')

languages = ['c/c++', 'c#', 'python', 'java']
print(languages.index('python'))

for idx, item in enumerate(languages):
    print(f'{idx}, {item}')

hobby = ['독서', '등산', '요리']
hobby
hobby.append('밥먹기')
hobby[3]
hobby

numbers = [1, 2, 3, 4, 5, 7, 8, 9]
numbers
numbers.insert(5, 6)
numbers
numbers.insert(9, 10)
numbers

weather = ['The', 'weather', 'very']
weather.insert(2, 'is')
weather.insert(4, 'cold')

# 성적 처리 프로그램
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

# 대충 반복문
for i in range (3):
    name = input('이름은? ')
    names.append(name)

    kor = int(input('국어는? '))
    kors.append(kor)

    eng = int(input('영어는? '))
    engs.append(eng)

    mat = int(input('수학은? '))
    mats.append(mat)

    tot = kors[i] + engs[i] + mats[i]
    # tots[i] = kors[i] + engs[i] + mats[i]
    tots.append(tot)

    avg = tots[i] / 3
    avgs.append(avg)

    grds.append('가')
    if avgs[i] >= 90: grds[i] = '수'
    if avgs[i] >= 80: grds[i] = '우'
    if avgs[i] >= 70: grds[i] = '미'
    if avgs[i] >= 60: grds[i] = '양'

    print(' 입력 완료!')

for i in range(3):
    print(f'{names[i]}, {kors[i]}, {engs[i]}, {mats[i]}\n'
          f'{tots[i]}, {avgs[i]}, {grds[i]} ')
print(names)
print(kors)
print(engs)
print(mats)
print(tots)
print(avgs)
print(grds)

# 리스트 수정 >>>  리스트이름[수정할위치(0부터 시작임!)] = 수정할 값
hobby
hobby[1] = '여행'
hobby

# 리스트 삭제
# >>> pop() : 맨마지막 삭제?
hobby
hobby.pop()
hobby
# >>> pop(삭제할위치) : 그 위치의 값 삭제?
hobby.pop(3)

# >>> remove(이름) : 이름으로 항목 제거
hobby.remove('밥먹기')


# 과일리스트에서 야채 삭제하기
fruits = ['사과','망고','당근','수박','포도','참외','토마토']

# 위치 값으로 삭제
fruits
fruits.pop(2)
# fruits.remove('당근') 위에 꺼랑 같은거임

# 값으로 삭제
fruits
fruits.remove('토마토')
fruits.remove('당근')
fruits



# 합격 여부 알아보기
gong = [55, 35, 40, 70, 65, 30]
gong[1]
four = 0
for i in range(6+1):
    if (gong[i] < 40):
        four += 1
    else:
        sum = int(gong[0] + gong[1] + gong[2] + gong[3] + gong[4] + gong[5])
        avg = sum / 6
    if (four > 0 and avg < 60):
        you = '아쉽습니다. 불합격입니다'
    else:
        you = '합격을 축하드립니다'

print(f'40점 미만 과목수 : {four} \n'
      f'평균점수 : {avg}\n'
      f'{you}')

gong = [55, 35, 40, 70, 65, 30]
gong = [55, 90, 40, 70, 65, 100]
cnt = len(gong)
sum = 0
fails = 0
result = '아쉽습니다. 불합격하셨습니다'

for i in range(cnt):
    if gong[i] < 40:
        fails += 1 # 과락수 증가
    sum += int(gong[i])
avg = sum / cnt
if fails == 0 and avg >= 60:
    result = '축하합니다. 합격하셨습니다'

print(f'평균점수 : {avg: .2f}')
print(result)

# 정렬하기
numbers = [5,1,3,4,2,6]
numbers.sort()
numbers
numbers.sort(reverse=True)

# 모의 고사 점수 정렬
score = [90,100,88,85,95,92,70,75,100,92,78,80,75,95,90,100,84]
score.sort()
score.sort(reverse=True)
score

# 문자 정렬 (한글)
names = ['길동','희동','둘리','또치','도우너']
names.sort()
names.sort(reverse=True)
names.reverse()

names


# 문자 정렬 (영어)
units = ['probe','zealot','dragoon','dark templer','high templer','scout','reaver']
units.reverse()

# [a:b] a 부터 b-1 까지
# [:b] a 빼면 0부터 시작
# [a:] b 빼면 a부터 끝까지
# [a:] b 빼면 a부터 끝까지

# 리스트 슬라이싱
alphabet = ['a','b','c','d','e','f','g','h','i','j']
alphabet.reverse()
alphabet

alphabet[2:5+1] # 2 ~ 5 까지 추출

alphabet[:4+1] # 0 ~ 4 까지 추출
alphabet[0:4+1] # 0 ~ 4 까지 추출

alphabet[3:7+1] # 3 ~ 7 까지 추출

alphabet[5:] # 5 부터 추출
alphabet[5:9+1] # 5 부터 추출

alphabet[3:8+1] # 3 ~ 8 까지 추출

alphabet[6:] # 6 부터 끝까지 추출
alphabet[-4:] # 뒤에서 4개? 대충 위에꺼랑 같다

# 대충 abcd 추출해보기
alphabet[:-6]

# 대충 dcba 추출해보기 // 슬라이싱 고급기능
alphabet[3::-1]
alphabet[-7::-1]
alphabet [-7:-11:-1]
alphabet[:-3:-1]
alphabet [0:4:-1] # 역순방향?

