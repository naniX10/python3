# 열차 교차 시간
for i in range(1, 541):
    if (i % 10 == 0 and i % 25 == 0):
        i
    elif (i % 10 == 0 and i % 30 == 0):
        i
    elif (i % 25 == 0 and i % 30 == 0):
        i
    else:
        continue

    print(f'{9 + (i // 60)}시 {(i % 60)}분 ')



train1 = 10
train2 = 25
train3 = 30

for i in range(1, 540+1):
    # 분을 시간으로 분리해서 출력
    hour = (i // 60) + 9
    min = i % 60

    if (i % train1 == 0 and i % train2 == 0):
        print(f'A와 B 충돌! {hour}시 {min}분')
    elif (i % train2 == 0 and i % train3 == 0):
        print(f'B와 C 충돌! {hour}시 {min}분')
    elif (i % train3 == 0 and i % train1 == 0):
        print(f'C와 A 충돌! {hour}시 {min}분')




