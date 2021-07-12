from EMP import EMP
from EMPService import EMPService

emp = EMP(1001, 'Michael', 'Jackson', 'MJ@gmail.com', '1231231230',
               '2002-01-05', 'AD_PRES', 50000, '', '', 1)

print(emp)

# empsrv = EMPService() # 객체 생성
# emp = empsrv.readEmp() # 메서드 호출
# print(emp)

emp = EMPService.readEmp()  # 객체생성없이 바로 메서드 호출
print(emp)

###
from datetime import datetime
#
# now = datetime(2021,7,12)
# hire = datetime(2002,1,5)
#
# days = now - hire # 근무일수
# print(days)

EMPService.computeDuty(emp)
