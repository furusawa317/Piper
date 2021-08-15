import numpy as np
import scraping_t

## アレイ化
# 気温
temp_array_t = np.array(scraping_t.temp_t, dtype=float)
#print(temp_array)

# 湿度
humid_array_t = np.array(scraping_t.humid_t, dtype=float)
#print(humid_array)

## 不快指数の計算
# 不快指数＝0.81×温度+0.01×湿度x（0.99×温度－14.3）+46.3
f_index_array_t = 0.81 * temp_array_t + 0.01 * humid_array_t * (0.99 * temp_array_t - 14.3) + 46.3
#print(f_index_array)

# 不快指数のリスト化
f_index_t = f_index_array_t.tolist()

#print(f_index_t)

