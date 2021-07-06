# 대충 로그인

for i in range(1, 6+1):
    pwd = input('암호를 입력해 주세요 ')

    if (pwd == 'hanbitac'):
        print('로그인 됐습니다')
        break
    else :
        print('암호를 다시 확인하세요!')
        pwd = input('암호를 입력해 주세요 ')

else:
    print('로그인 실패! 횟수 초과!')


userid = input('아이디를 입력해주세요!')
passwd = input('비밀번호를 입력해주세요!')

if userid == 'admin' and passwd == 'hanbitac':
    print('로그인 되었습니다')
else:
    print('암호를 확인하세요')

for i in range(5):
    userid = input('아이디를 입력해주세요!')
    passwd = input('비밀번호를 입력해주세요!')

    if userid == 'admin' and passwd == 'hanbitac':
        print('로그인 되었습니다')
        break
    else:
        print('암호를 확인하세요')
else:
    print('로그인 실패! 횟수 초과!')

cnt = 1

while True:
    if cnt > 5:
        print('로그인 실패! 횟수 초과')

    userid = input('아이디를 입력해주세요!')
    passwd = input('비밀번호를 입력해주세요!')

    if userid == 'admin' and passwd == 'hanbitac':
        print('로그인 되었습니다')
        break
    else:
        print('암호를 확인하세요')
    cnt += 1
