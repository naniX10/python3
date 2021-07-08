# 상품 할인률 계산
# 1개 > 5% / 2개 > 10% / 3개 > 20% / 4개이상 > 30%

def checkDiscount(goods):
    rate = 0.3
    sum = 0

    if len(goods) == 1:
        rate == 0.005
    elif len(goods) == 2:
        rate = 0.1
    elif len(goods) == 3:
        rate = 0.2

    for i in range(len(goods)):
        sum += goods[i]

    fare = sum * (1 - rate)

    print(f'할인률 : {rate}')
    print(f'총 구매 금액 : {sum}')
    print(f'할인 적용금액 : {fare}')

def discountGoods():
    goods = []

    flag = True

    while flag:
        job = input('원하시는 작업을 선택하세요\n'
                    '1. 구매 2. 종료')

        if job == '1':
            price = int(input('구매한 상품의 가격을 입력하세요'))
            goods.append(price)



        elif job == '2':
            flag = False
            checkDiscount(goods)

        else:
            print('잘못 입력하셨습니다!!')
