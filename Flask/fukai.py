import numpy as np
import scraping

## アレイ化
# 気温
temp_array = np.array(scraping.temp, dtype=float)
#print(temp_array)

# 湿度
humid_array = np.array(scraping.humid, dtype=float)
#print(humid_array)

## 不快指数の計算
# 不快指数＝0.81×温度+0.01×湿度x（0.99×温度－14.3）+46.3
f_index_array = 0.81 * temp_array + 0.01 * humid_array * (0.99 * temp_array - 14.3) +46.3
#print(f_index_array)

# 不快指数のリスト化
f_index = f_index_array.tolist()

#print(f_index)
