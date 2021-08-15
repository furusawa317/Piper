import numpy as np
import requests
import bs4

URL = 'https://tenki.jp/forecast/1/2/1400/1108/1hour.html'

r = requests.get(URL)
s = bs4.BeautifulSoup(r.text, 'html.parser')

## 気温の取り込み
# 気温リストの作成
list_temp= []

#入れ子の要素取得（取得要素の絞り込み）
for j in s.find_all('tr' , class_ ='temperature'):
    for i in j.find_all("span"):
        list_temp.append(i.string)

temp = []
for i in range(0,24,1):
#    print(list_temp[i])
    temp.append(list_temp[i])

## 湿度の取り込み
#湿度リストの作成
list_humid= []

#入れ子の要素取得（取得要素の絞り込み）
for j in s.find_all('tr' , class_ ='humidity'):
    for i in j.find_all("span"):
        list_humid.append(i.string)

humid=[]
for i in range(1,25,1):
#    print(list_humid[i])
    humid.append(list_humid[i])

## アレイ化
# 気温
temp_array = np.array(temp, dtype=float)
#print(temp_array)

# 湿度
humid_array = np.array(humid, dtype=float)
#print(humid_array)

## 不快指数の計算
# 不快指数＝0.81×温度+0.01×湿度x（0.99×温度－14.3）+46.3

f_index_array = 0.81 * temp_array + 0.01 * humid_array * (0.99 * temp_array - 14.3) +46.3

#print(f_index_array)

# 不快指数のリスト化
f_index = f_index_array.tolist()

#print(f_index)


# 現在の不快指数（予報）の表示
import datetime
dt_now = datetime.datetime.now()
time = int(dt_now.strftime('%H'))
#print(f_index[time])

now_f_index = f_index[time]
print(now_f_index)

# 現在の不快指数（予報）による分岐
if now_f_index < 55:
    i = 0
elif now_f_index < 60:
    i = 1
elif now_f_index < 65:
    i = 2
elif now_f_index < 70:
    i = 3
elif now_f_index < 75:
    i = 4
elif now_f_index < 80:
    i = 5
elif now_f_index < 85:
    i = 6
elif now_f_index >= 85:
    i = 7

# 不快指数コメント用リスト
f_comment = ["寒い", "肌寒い", "何も感じない", "快い", "暑くない", "やや暑い", "暑くて汗がでる", "暑くてたまらない"]

# 画像用辞書
f_images = {
    0:"https://1.bp.blogspot.com/-m95-Y5UgJjs/WzC95dS6Q_I/AAAAAAABM80/25DbWYUQitAMj64PMC_InvorlgCXlCUNACLcBGAs/s800/samui_man.png",
    1:"https://1.bp.blogspot.com/-75o6nIlKdLQ/Wb8gcEXupII/AAAAAAABGxo/PCZ6Zl4k0cQVXzqZJFQmvx-X32hzIthtwCLcBGAs/s800/kisetsukan_nai_man.png",
    2:"https://3.bp.blogspot.com/-mpmeOXs__m8/XDXcqKgGhNI/AAAAAAABRL8/r_PuY6N931sNUzAB6zkiQgiVZDcOWolBgCLcBGAs/s800/sleep_gorogoro_man.png",
    3:"https://2.bp.blogspot.com/-ewr_OVkqqbc/V6wGUBMD84I/AAAAAAAA9Dw/JaxdpzH2z0gwnQX5F5UjmbxmPd0y5DXqwCLcB/s800/stand_woman_summer.png",
    4:"https://1.bp.blogspot.com/-urokhQ_hWZs/W1qdcMqqCBI/AAAAAAABNqU/NaU_9ar2kI80aKM40RZTO6kaU80eywMHgCLcBGAs/s800/kokage_tree_necchusyou_drink.png",
    5:"https://1.bp.blogspot.com/-AdxpSuw14c0/XPjWRe-2YGI/AAAAAAABTCQ/JQZsGqk3zagUYZV8VTKhdppAIUPKdL6twCLcBGAs/s800/summer_uchiwa_man.png",
    6:"https://2.bp.blogspot.com/-hTLmh2ufYwQ/W1qdgDHLvpI/AAAAAAABNqo/1SyIGiEznGM8J69x0GUln60R1DotiI5MQCLcBGAs/s800/sick_atsui_businessman.png",
    7:"https://4.bp.blogspot.com/-E7a2JiOK770/UrEgC4QPotI/AAAAAAAAb2s/Ucoh7CD2y2k/s800/nettaiya.png"
}

print("現在の不快指数は" + str(now_f_index) + "で『" + f_comment[i] + "』状態です。")
print(f_images[i])
