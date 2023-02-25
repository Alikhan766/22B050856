from datetime import date, timedelta
ys = date.today() - timedelta(1)
td = date.today()
tm = date.today() + timedelta(1)
print('Yesterday', ys)
print('Today', td)
print('Tomorrow', tm)
