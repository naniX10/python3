# 날씨 예보?
date = input('날짜를 입력해주세요\n')
day = input('요일을 입력해주세요\n')
mortem = int(input('아침기온을 입력해주세요\n'))
nottem = int(input('낮기온을 입력해주세요\n'))
rainper = int(input('비가 올 확률을 입력해주세요\n'))
micro = input('미세먼지 수치를 입력해주세요(좋음,보통,나쁨,매우나쁨 중에 하나)\n')
sunrise = input('일출시간을 입력해주세요\n')
sunset = input('일몰시간을 입력해주세요\n')
sousea = float(input('남해의 파고를 입력해주세요\n'))
eassea = float(input('동해의 파고를 입력해주세요\n'))
wessea = float(input('서해의 파고를 입력해주세요\n'))

print('-------------------------------------------------------------')
print('내일 날씨 예보입니다')
print(day + '요일인 ' + date + '의 아침 최저 기온은 '
      + str(mortem) + '도, 낮 최고 기온은 ' + str(nottem) + '도로 예상됩니다')
print('비 올 확률은 ' + str(rainper) + '%이고, 미세먼지는 ' + micro +
      '수준으로 예상됩니다')
print('일출 시간은 ' + sunrise + '이고, 일몰시간은 '
      + sunset + '입니다.')
print('파고는 남해 앞바다 ' + str(sousea) +
      'm, 동해 앞바다 ' + str(eassea) + 'm, 서해 앞바다 ' + str(wessea) +
      'm 높이로 일겠습니다.')
print('지금까지 ' + date + ' ' + day + '요일 날씨 예보 였습니다')
print('-------------------------------------------------------------')

print('-------------------------------------------------------------')
print('내일 날씨 예보입니다')
print('{0}요일인 {1} 의 아침 최저 기온은 {2}도, 낮 최고 기온은 {3}도로 예상됩니다'
      .format(day, date, mortem, nottem))
print('비 올 확률은 {0}%이고, 미세먼지는 {1}수준으로 예상됩니다'.format(rainper, micro))
print('일출 시간은 {0}이고, 일몰시간은 {1}입니다.'.format(sunrise, sunset))
print('파고는 남해 앞바다 {0}m, 동해 앞바다 {1}m, 서해 앞바다 {2}m 높이로 일겠습니다.'
      .format(sousea, eassea, wessea))
print('지금까지 {0} {1}요일 날씨 예보 였습니다'.format(date, day))
print('-------------------------------------------------------------')

print('-------------------------------------------------------------')
print('내일 날씨 예보입니다')
print('%s요일인 %s 의 아침 최저 기온은 %d도, 낮 최고 기온은 %d도로 예상됩니다'
      % (day, date, mortem, nottem))
print('비 올 확률은 %d퍼센트고, 미세먼지는 %s수준으로 예상됩니다' % (rainper, micro))
print('일출 시간은 %s이고, 일몰시간은 %s입니다.' % (sunrise, sunset))
print('파고는 남해 앞바다 %.1fm, 동해 앞바다 %.1fm, 서해 앞바다 %.1fm 높이로 일겠습니다.'
      % (sousea, eassea, wessea))
print('지금까지 %s %s요일 날씨 예보 였습니다' % (date, day))
print('-------------------------------------------------------------')



print('-------------------------------------------------------------')
print('내일 날씨 예보입니다\n' + day + '요일인' + date + '의 아침 최저 기온은 '
      + mortem + '도, 낮 최고 기온은 ' + nottem + '도로 예상됩니다\n'
      + '비 올 확률은 ' + rainper + '%이고, 미세먼지는 ' + micro +
      '수준으로 예상됩니다\n' + '일출 시간은 ' + sunrise + '이고, 일몰시간은'
      + sunset + '입니다.\n' + '파고는 남해 앞바다 ' + sousea +
      'm, 동해 앞바다 ' + eassea + 'm, 서해 앞바다 ' + wessea +
      'm 높이로 일겠습니다.\n' + '지금까지 ' + date + day +
      '요일 날씨 예보 였습니다')
