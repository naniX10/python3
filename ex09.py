# 생존률 출력
time = int(input('최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요. '))
if (time < 60):
    survive = '85%'
elif (time < 120):
    survive = '76%'
elif (time < 180):
    survive = '66%'
elif (time < 240):
    survive = '57%'
elif (time < 300):
    survive = '47%'
else:
    survive = '25% 미만'
print(f'생존률 : {survive}')

