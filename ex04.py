import operator as op

# 수온 측정...
deep = int(input('수심을 입력하세요.'))
temp = (20 - ((deep // 10) * 0.7))
print(f'수온 : {temp}')



# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램을 작성해보세요
vita = int(input('(1 ~ 9) 사이 숫자를 하나를 입력해주세요'))
print(f'{vita} X 1 =  {vita * 1}')
print(f'{vita} X 2 =  {vita * 2}')
print(f'{vita} X 3 =  {vita * 3}')
print(f'{vita} X 4 =  {vita * 4}')
print(f'{vita} X 5 =  {vita * 5}')
print(f'{vita} X 6 =  {vita * 6}')
print(f'{vita} X 7 =  {vita * 7}')
print(f'{vita} X 8 =  {vita * 8}')
print(f'{vita} X 9 =  {vita * 9}')

#키보드로 정수를 하나 입력받아 그 값이 정수, 음수, 0인지 구분하는 프로그램을 작성하시오.
# 각각의 경우에 따라 “정수입니다”, “음수입니다”, “0입니다”라고 출력하도록 한다.
num = int(input('정수를 하나 입력해주세요'))
res = '양수입니다' if (num > 0) else\
      '0 입니다' if (num == 0) else '음수입니다'
print(res)

# 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라 가정할 때,
# 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을 작성하세요
money = 2_5000
rate = 6.0
