# 파일 다루기



# 입력한 데이터를 파일에 저장
fname = 'c:/java/sungjuk.dat'

name = input('이름은? ')
kor = int(input('국어는? '))
eng = int(input('영어는? '))
mat = int(input('수학은? '))

f = open(fname, 'w') # 지정 파일을 쓰기 모드 엶

# data = 'Hello, World!!'
data = f'{name} {kor} {eng} {mat}'
# 파일에 기록할 내용을 문자열로

f.write(data)
f.close()


# 기록한 데이터 파일을 읽어오기
f = open(fname, 'r')
data = f.read()
print(data)
f.close()

# 메모 입력
fname = 'c:/java/memo.txt'

contents = input('내용을 입력하세요')

f = open(fname, 'w')
data = f'{contents}'

f.write(data)
f.close()


def saveMemo(memo):
    fname = 'c:/java/memo.txt'
    f = open(fname, 'a') # 추가append 모드로 파일을 초기화
    f.write(memo + "\n")
    f.close()


def memoMain():
    memo = input('내용을 입력하세요')
    saveMemo(memo)

memoMain()


# py 3 방식으로 파일다루기
# 기존 파일 입출력모드에서 불편한 점은
# 파일작업 후에 반드시 close를 해야한다는 것
# with문을 사용하면 명시적으로 close를 사용하지 않아도 됨

with open(fname, 'w') as f:
    f.write('!@#$%%!!Q')

# 파일에서 데이터 읽어오기
fname = 'c:/java/emp.csv'

with open(fname) as f:
    data = f.read() # 모든 데이터를 한번에!
    print(data)

with open(fname) as f:
    data = f.readline() # 한줄만 읽어오기
    print(data)

with open(fname) as f:
    data = f.readlines() # 모든데이터를 라인단위로 읽어와서
    print(data)          # list 형태로 저장

# emp.csv에서 사번, 이름, 입사일, 급여를 출력
with open(fname) as f:
    f.readline() # 첫줄은 읽기만 함
    while True:
        line = f.readline()
        if not line:
            break # 읽을 데이터가 없으면 종료
        data = line.split(',') # 문자열을 ,로 분리해 저장

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])


        emp = f'{empno} {name} {hdate} {sal:,}'
        print(emp)

#  타이타닉 데이터셋을 이용
# 승객이름name 성별sex 나이age
# 승선위치embarked 사망여부survivied 등을 추출해서 출력하세요
# 단, survivied가 0이면 사망 1이면 생존이라 출력1234 10
# 단, embarked가 S면 southampthon c이면 cherbourg이라
# q 면 queenstown 이라 출력

fname = 'c:/java/titanic3b.csv'

with open(fname) as f:
    f.readline() # 첫줄은 읽기만 함
    while True:
        row = f.readline()
        if not row:
            break # 읽을 데이터가 없으면 종료

        data = row.split(',') # 문자열을 ,로 분리해 저장

        # name = data[2]
        sex = data[2]
        age = data[3]
        pos = data[9]
        live = data[1]

        if pos == 'S' :
            pos = 'southampthon'
        elif pos == 'Q':
            pos = 'queenstown'
        elif pos == 'C':
            pos = 'cherbourg'

        if live == '0' :
            live = '사망'
        elif live == '1':
            live = '생존'

        if age == '':
            age ='0'

        result = f' {sex} {age} {pos} {live}'
        print(result)

