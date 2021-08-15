import fukai_t
import datetime

# 現在の不快指数（予報）の表示
dt_now = datetime.datetime.now()
time = int(dt_now.strftime('%H'))
#print(f_index[time])

now_f_index_t = round(fukai_t.f_index_t[time])
#print(now_f_index_t)

# 現在の不快指数（予報）による分岐
if now_f_index_t < 55:
    m = 0
elif now_f_index_t < 60:
    m = 1
elif now_f_index_t < 65:
    m = 2
elif now_f_index_t < 70:
    m = 3
elif now_f_index_t < 75:
    m = 4
elif now_f_index_t < 80:
    m = 5
elif now_f_index_t < 85:
    m = 6
elif now_f_index_t >= 85:
    m = 7

#print(m)