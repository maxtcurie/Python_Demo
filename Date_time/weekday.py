from datetime import datetime

#monday 1, .... sunday 7
print(datetime.today())
print(datetime.today().weekday())
print(datetime.today().isoweekday())

d1 = datetime.strptime('2018-12-31 21:12:59', "%Y-%m-%d %H:%M:%S")
print(d1)
print(d1.weekday())
print(d1.isoweekday())