# 문자열은 문자들의 리스트와 유사
# 따라서, 리스트 슬라이싱을 통해 문자열내
# 개별문자를 추출할 수 있음

# '파이썬완전재밌어요'에서 홀수 위치에 있는 문자대신
# <#> 을 출력하는 코드를 작성

str= '파이썬완전재밋어요'
print(str)

for i in range(len(str)):
    if i % 2 == 0:
        print(str[i], end='')
    else:
        print('#', end='')
print()

# 문자열 함수
# 대소문자 변환
str = 'Python is Easy. 그래서 pro드래밍이 재밋어요'

str.lower()
str.upper()
str.swapcase()
str.title()

# 문자열 찾기
str = '파이썬 공부는 재밋어요! 물논 공부보다 노는게 더 재밋지만...'

str.count('공부') # 특정 문자열 포함 갯수
str.find('공부') # 문자열을 찾은 위치(왼쪽 기준)
str.find('공부', 5) # 특정인덱스를 기준점으로 문자열을 찾은 위치(왼쪽 기준)
str.find('공부', str.find('공부') + 1)
str.find('ㅇㅅㅇ') # 찾지 못하는 경우 > -1
str.rfind('공부') # 문자열을 찾은 위치(오른쪽 기준)

str.index('공부')
str.index('공부', 5)
str.rindex('공부')
str.index('ㅇㅅㅇ') # 찾지 못하면 오류!

str.startswith('파이썬') # 특정 문자열로 시작하는지?
str.startswith('파이썬', 10) # 특정 인덱스 이후로 특정 문자로 시작하는지?
str.startswith('물논', 14)
str.endswith('...') # 특정 문자열로 끝나는지?

# 문자열 안의 공백 다루기
str = '  파  이  썬  '
str.strip()   # 공백제거 : 매개변수 없음
str.rstrip()
str.lstrip()

str = '--파---이---썬--'
str.strip('-')   # 지정문자 제거 : 매개변수로 제거할 문자 지정
str.rstrip('-')
str.lstrip('-')

str = '<<파 << 이 >> 썬>>'
str.strip('<>')   # 지정문자들 제거 : 매개변수로 제거할 문자열 지정
str.rstrip('<>')
str.lstrip('<>')


str = '열심히 파이썬 공부중~'
str.replace('파이썬','Python')   # 지정한 문자열을 새로운 문자열로 바꿈


str = '  파  이  썬  '
str.replace(' ', '')

str = '--파---이---썬--'
str.replace('-', '')

str = '<<파 << 이 >> 썬>>'
str = str.replace('<', '')
str = str.replace('>', '')
str.replace(' ', '')


# 문자열 분리 결합
str = '길동,100,40,100' # 구분기호로 문자열을 분리하고 리스트 로 저장
str.split(',')

str = '길동|100|40|100'
str.split('|')

str = '길동\r\n100\r\n40\r\n100'
str.split('\r\n')
str.splitlines()

str = ['길동','100','40','100']
','.join(str) # 리스트의 각 항목을 구분기호로 결합

result = ''
for s in str:
    result += s + ','

# 객체를 특정함수에 일괄적으로 적용
# map(적용할함수명, 대상객체
str = ['123','456','789'] # 문자열을 숫자로 변경

nums = [] # map을 사용하지 않을 때
for s in str:
    nums.append(int(s))

nums = list(map(int, str))

# 문자열 정렬

# 특정문자로 채우기

# 문자열 구성 파악

# 입력한 값이 한글,영어면 글자 / 숫자면 숫자 / 섞여있으면 숫자+글자
# 그외 나머지는 모르겠습니다 라고 출력력
str = input('문자열을 입력해주세요 ')

result = ''
if str.isalpha(): result = '글자입니다'
elif str.isdigit(): result = '숫자입니다'
elif str.isalnum(): result = '글자+숫자입니다'
else: result = '모루겟소요'

print(result)

