import operator as op
# 속도, 시간에 따른 주행거리 계산
speed = int(input('주행속도 : '))
hour = int(input('주행시간 : '))
km = op.mul(speed, hour)
print(f'주행 이동 거리 : {km}')