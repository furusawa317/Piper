import fukai_h

now_f_index_h = round(fukai_h.f_index_h)
#print(now_f_index_h)

# 現在の不快指数（予報）による分岐
if now_f_index_h < 55:
    h = 0
elif now_f_index_h < 60:
    h = 1
elif now_f_index_h < 65:
    h = 2
elif now_f_index_h < 70:
    h = 3
elif now_f_index_h < 75:
    h = 4
elif now_f_index_h < 80:
    h = 5
elif now_f_index_h < 85:
    h = 6
elif now_f_index_h >= 85:
    h = 7

#print(h)