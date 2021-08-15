import fukai
import datetime

# 現在の不快指数（予報）の表示
dt_now = datetime.datetime.now()
time = int(dt_now.strftime('%H'))
#print(f_index[time])

now_f_index = round(fukai.f_index[time])
print(now_f_index)

# 現在の不快指数（予報）による分岐
if now_f_index < 55:
    n = 0
elif now_f_index < 60:
    n = 1
elif now_f_index < 65:
    n = 2
elif now_f_index < 70:
    n = 3
elif now_f_index < 75:
    n = 4
elif now_f_index < 80:
    n = 5
elif now_f_index < 85:
    n = 6
elif now_f_index >= 85:
    n = 7

print(n)