# 업무용 컴, 업무 시간
work = int(input('근무 시간을 입력하세요 '))
com1 = (24 // work)
com2 = (24 % work)
res = (com1 + 1) if (com2 != 0) else com1
print(f'필요한 컴퓨터: {res}')

computer = 3 * 8 //work