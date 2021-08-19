import temphumid_h

## 不快指数の計算
# 不快指数＝0.81×温度+0.01×湿度x（0.99×温度－14.3）+46.3
f_index_h = 0.81 * temphumid_h.h_temp + 0.01 * temphumid_h.h_humid * (0.99 * temphumid_h.h_temp - 14.3) + 46.3

#print(f_index_h)
