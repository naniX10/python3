# 직책이 IT_PROG인 사원들의 사번 성 입사일을 출력하는 코드를 작성
import sqlite3

import pymysql
conn = pymysql.connect(host = 'bigdata.cqpzprjlgsfx.ap-northeast-2.rds.amazonaws.com',
                       charset = 'utf8', user = 'playground',
                       password = 'bigdata2020', db = 'playground' )

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = " select EMPLOYEE_ID, LAST_NAME, Hire_DATE from EMPLOYEES where job_id = 'IT_PROG' "

cursor.execute(sql)
rows = cursor.fetchall()

cursor.close()
conn.close()

for row in rows:
    print(row['EMPLOYEE_ID'], row['LAST_NAME'], row['Hire_DATE'])

# 30번 부서의 사원수를 조회하는 코드 작성
conn = pymysql.connect(host = 'bigdata.cqpzprjlgsfx.ap-northeast-2.rds.amazonaws.com',
                       charset = 'utf8', user = 'playground',
                       password = 'bigdata2020', db = 'playground' )

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = ' select count(LAST_NAME) cnt from EMPLOYEES where DEPARTMENT_ID = 30 '

cursor.execute(sql)
rows = cursor.fetchone() # 대충 count는 값이 하나니까 fetchone으로 가져오라는 설명

cursor.close()
conn.close()

# 단일 값이므로 for문 없이 바로 출력
print(rows['cnt'])


# 데이터 삽입
import sqlite3
conn = sqlite3.connect('c:/java/sqlite3/nanix10.db')

# 접속후 커서를 가져옴
cur = conn.cursor()

# 질의문 작성
sql = 'select pcode, pname, price, amount from product'
pcode = '12345'
pname = '에어컨'
price = '50'
amount = 10
sql = ' insert into product values ' \
      f' ("{pcode}","{pname}",{price},{amount}) '

# 질의문 실행 1
cur.execute(sql)

# 질의문 작성 2 - sqlite 3 미지원
sql = ' insert into product values (%s, %s, %d, %d)'
param = (pcode, pname, price, amount)

# 질의문 실행 2
cur.execute(sql, param)

# 실행한 내용을 서버에 반영
conn.commit()

# 작업종료
cur.close()
conn.close()

# 이름, 국어, 영어, 수학을 입력받아 sungjuk 테이블에 저장
import pymysql
conn = pymysql.connect(host = 'bigdata.cqpzprjlgsfx.ap-northeast-2.rds.amazonaws.com',
                       charset = 'utf8', user = 'playground',
                       password = 'bigdata2020', db = 'playground' )

cursor = conn.cursor(pymysql.cursors.DictCursor)

name = input('이름을 입력하세요')
kor = input('국어 성적을 입력하세요')
eng = input('영어 성적을 입력하세요')
mat = input('수학 성적을 입력하세요')

sql = ' insert into sungjuk (name, kor, eng, mat) values (%s, %s, %s, %s) '
param = (name, kor, eng, mat)

cnt = cursor.execute(sql, param)
print('입력한 데이터 건수 : ', cnt)

conn.commit()

cursor.close()
conn.close()




