import home_temp

## 不快指数の計算
# 不快指数＝0.81×温度+0.01×湿度x（0.99×温度－14.3）+46.3
f_index_h = 0.81 * float(home_temp.home_temp[0]) + 0.01 * float(home_temp.home_temp[1]) * (0.99 * float(home_temp.home_temp[0]) - 14.3) + 46.3

print(f_index_h)
