# 딕셔너리 키: 값 >>> 키는 중복 불가!!!
ages = {'박찬호':48, '박지성':40, '박세리': 50, '이승엽': 43}
ages
type(ages)

person = {'이름':'고길동', '나이':37, '몸무게':77, '주소':'서울 종로구 세종로',
          '취미':['운동','독서','음악감삼']}

sungjuk = {'c/c++':'A', 'JAVA':'B+', '네트워킹':'C', '보안':'A+', '해킹':'F', '시스템':'C+', }
sungjuk

person['나이']
person['취미']

# 혈액형 추가
# dict에 새로운 항목을 추가할 때는 새로운 키와 값으로 구성해야함
# dict에 기존 키와 값으로 구성한 항목을 추가하려 하면 기존키에 저장된 값이 수정됨
person['혈액형'] = 'O'
person

# 아이템 삭제 >> pop
#  딕셔너리이름.pop('삭제할 키 이름')
person.pop('혈액형') #

# 여러개 삭제하고 싶으면 반복문 써라?
dellist = ['나이','취미']
for key in dellist:
    person.pop(key)

# 조회하려면 keys(), values() 로 출력가능?
person = {'이름':'고길동', '나이':37, '몸무게':77, '주소':'서울 종로구 세종로',
          '취미':['운동','독서','음악감삼']}

for key in person.keys():
    print(person[key])

# dict의 키와 값 모두 가져오기 : items
person.items()

for k, v in person.items():
    print(k, v)

# 중간고사 성적 관리 프로그램 만들기
middle = {'C/C++':'A', 'JAVA':'B+', '모바일':'C', '보안':'A+', '해킹':'F', '시스템':'C+'}

# 자바, 시스템 조회?
middle['JAVA']
middle['시스템']

middle['파이썬'] = 'A'
middle['OS'] = 'A+'

middle['JAVA'] = 'F'
middle['시스템'] = 'A'

for k, v in middle.items():
    print(f'{k} : {v}', end=', ')

# 딕셔너리 for 축약문
# { 키 / 값 표현식 for 키, 값 in zip(반복가능객체1, 반복가능객체2) }
name = ['민정', 'ㅇㅇ', 'ㅎㅎ'] # 키
grd = ['수' , '미', '가'] # 값
sj = {}

# 반복문 안 씀
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

# 반복문 씀
for i in range(3):
    sj[name[i]] = grd[i]

# 반복문 축약?
# { 키 / 값 표현식 for 키, 값 in zip(반복가능객체1, 반복가능객체2) }
sj2 = { key:val for key,val in zip(name, grd) }

# zip 함수 >>> 여러개의 데이터를 하나로 합쳐서 iterable한 객체로 생성해 중 - 개별객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)

# 문제 출제, 채점 프로그램 ?
ques = ('3+2','5÷2의 몫','10-2','10²×2','1-(10÷4의 나머지)','2⁴','4÷2')
ans = ('5','2','8','200','-1','16','2')
score = ('3','5','3','5','5','3','3')
aans2 = []

for i in range(len(ques)):
    print(f'문제: {ques[i]} ' )
    ans2 = input('정답을 입력하세요')
    aans2.append(ans2[i])

# 회원가입
login = {}

while True:
    yon = int(input('1. 회원가입 2. 프로그램 종료'))
    if (yon == 1):
        a = input('아이디?')
        b = input('비밀번호?')
        login[a] = b
        continue
    if (yon == 2):
        break
    for k, v in login.items():
        print(f'{k} : {v}', end=', ')








