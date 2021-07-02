# 성적처리프로그램 개량
# 이름, 국어, 영어, 수학을 입력 / 총점, 평균, 학점을 출력
name = input('당신의 이름은?')
kor = int(input('당신의 국어성적은?'))
eng = int(input('당신의 영어성적은?'))
mat = int(input('당신의 수학성적은?'))
sum = kor + eng + mat
avg = float(sum / 3)
grd = '수' if (avg >= 90) else \
      '우' if (avg >= 80) else \
      '미' if (avg >= 70) else \
      '양' if (avg >= 60) else '가'

print(f'{name}님의 국어성적은 {kor}점, 영어성적은 {eng}점, 수학성적은 {mat}점 입니다 \n' \
      f'따라서 총점은 {sum}점이며, 평균은 {avg:.1f}점, 학점은 {grd}입니다')

# operator 모듈을 이용하면 대량의 데이터 처리시 속도 향상이 존재함
import operator as op

op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3) # 정수 몫 : //
op.truediv(10, 3) # 실수 몫 : /
op.mod(10, 3)
op.pow(2, 10)

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)
x = op.eq(10, 20)
y = op.gt(10, 20)
op.and_(x, y)
op.or_(x, y)

# 재난 지원금 대상 여부
soduk = int(input('월 소득을 입력하세요.'))
jiwon = int(input('다른 지원금을 받고 있습니까? (1 > 받고있다 / 2 > 받고있지 않다)'))
jogun = op.and_(op.le(soduk, 400_0000), op.eq(jiwon, 2))
what = '수급대상자입니다' if jogun else '수급 대상자가 아닙니다'
print(what)

