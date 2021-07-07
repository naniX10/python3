# # 대충 혈액
# A = []
# B = []
# AB = []
# O = []
# for i in range(1,10+1):
#     blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 \n'
#                   'A, B, AB, O : ')
#     if (blood == 'A' or blood == 'a'):
#         A.append('A')
#     elif (blood == 'B' or blood == 'b'):
#         B.append('B')
#     elif (blood == 'AB' or blood == 'ab'):
#         AB.append('AB')
#     elif (blood == 'O' or blood == 'o'):
#         O.append('O')
#     else:
#         continue
# print('------------------- \n'
#       '  혈액형 : 개수 \n'
#       ' ------------------ \n'
#       f' A형 : {len(A)} \n'
#       f' B형 : {len(B)} \n'
#       f' AB형 : {len(AB)} \n'
#       f' O형 : {len(O)} \n')

# while True:
#     lll = input(' 1 or 2')
#     if (lll == '1'):
#         input()

bloods = []
for i in range(10):
    blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 \n'
                  'A, B, AB, O : ')
    bloods.append(blood)

print('-' * 100)
print('혈액형 : 개수 ')
print('-' * 100)
print(f' A형 : {bloods.count("A")} ')
print(f' B형 : {bloods.count("B")} ')
print(f' AB형 : {bloods.count("AB")} ')
print(f' O형 : {bloods.count("O")} ')
print('-' * 100)
