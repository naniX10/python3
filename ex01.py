# 비번 메일 발송 프로그램  / 한줄 한줄씩 print 써라?
email = input('당신의 이메일을 입력해주세요\n')
name = input('당신의 이름은?\n')
userid = input('당신의 아이디는?\n')
passwd = input('당신의 비밀번호는?\n')

print('To. ' + email + '\n' + '▶ 아이디 및 비밀번호 확인\n'
      + name + ' 고객님 안녕하세요.\n' + name +
      ' 고객님의 아이디와 비밀번호는 아래와 같습니다\n' +
      '아이디 : ' + userid + '\n'
      '비밀번호 : ' + passwd )
print('--------------------------')
# 출력시에 변수와 문자열 사이에 , 사용하면 공백이 하나 더 추가됨
print('To. ', email , '\n' + '▶ 아이디 및 비밀번호 확인\n'
      , name, ' 고객님 안녕하세요.\n', name,
      ' 고객님의 아이디와 비밀번호는 아래와 같습니다\n' +
      '아이디 : ', userid, '\n'
      '비밀번호 : ', passwd)
print('--------------------------')

# format 함수를 사용 : 문자열 템플릿으로 출력 파이썬 3
print('To. {0}'. format(email), '\n' + '▶ 아이디 및 비밀번호 확인\n'
      '{0} 고객님 안녕하세요.\n'.format(name)+
      '{0}고객님의 아이디와 비밀번호는 아래와 같습니다\n'.format(name)+
      '아이디 : {0}'.format(userid)+'\n' 
      '비밀번호 : {0}'.format(passwd))
print('--------------------------')

# format 함수 사용 파이썬2
print('To. %s' % email, '\n' + '▶ 아이디 및 비밀번호 확인\n'
      '%s 고객님 안녕하세요.\n' % name+
      '%s고객님의 아이디와 비밀번호는 아래와 같습니다\n'% name+
      '아이디 : %s' % userid+'\n' 
      '비밀번호 : %s' % passwd)
print('--------------------------')
