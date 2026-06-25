'''
from datetime import date,time,datetime,time
t=date.today()
print(t)
print("year:", t.year)
print("month:",t.month)
print("Day:",t.day)
print("weekday from 0:",t.weekday())
print("weekday from 1:",t.isoweekday())

#date validity:
from datetime import date,time,datetime,time
t=date(2026,12,30)

#time validity:
from datetime import date,time,datetime,time
t=time(11,28,16)
print(t)


#current date and time:
from datetime import date,time,datetime,time
n=datetime.now()
print(n)
print("year:",n.year)
print("month:",n.month)
print("Day:",n.day)
print("Hour:",n.hour)
print("minute:",n.minute)
print("second:",n.second)
print(t)

from datetime import date,time,datetime,time
n=datetime.now()
print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d/%B/%y %I:%M:%S %p'))
print(n.strftime('%d/%b/%y %I:%M:%S %p'))
print(n.strftime('%a/%B/%y %I:%M:%S %p'))
print(n.strftime('%A/%B/%y %I:%M:%S %p'))
'''

from datetime import date,time,datetime,timedelta
n=datetime.now()
n15 = n+ timedelta(minutes=15)
n2 = n+ timedelta(hours=2)
n7 = n+ timedelta(days=60)
print(n15,n2,n7,sep='\n')































