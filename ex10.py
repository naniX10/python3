# 전기요금
elec = int(input('전기 사용량을 입력하세요. '))
print(f'사용량 : {elec} kwh')
if (elec <= 200):
    base = 910
    per = 99.3
    price = (per * elec + base)
    print(f'기본요금 : {base:,} \n'
          f'단가 : {per} \n'
          f'전기 요금 : {price:,}')
elif (200 < elec <= 400):
    base = 1600
    per = 187.9
    price = (per * elec + base)
    print(f'기본요금 : {base:,} \n'
          f'단가 : {per} \n'
          f'전기 요금 : {price:,}')
else:
    base = 7300
    per = 280.6
    price = (per * elec + base)
    print(f'기본요금 : {base:,} \n'
          f'단가 : {per} \n'
          f'전기 요금 : {price:,}')

