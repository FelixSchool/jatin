import datetime

x = datetime.datetime(1999, 7, 29)


print(x.strftime("%B %dth %Y"))
print(x.strftime("%dth %B %Y"))
print(x.strftime("%B %d, %Y"))
print(x.strftime("%b-%d-%Y"))
print(x.strftime("%d-%m-%y"))
print(x.strftime("%d-%m-%Y"))
print(x.strftime("%d/%m/%Y"))
print(x.strftime("%B the %dst, the year %Y"))