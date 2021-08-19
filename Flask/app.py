import fukai_s
import hantei_s
import fukai_t
import hantei_t
import temphumid_h
import hantei_h

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

#print(humid_array[time])
#print(temp_array[time])

fukai1 = "現在の札幌市厚別区の気温は" + str(fukai_s.temp_array[hantei_s.time]) + "度、湿度は" + str(fukai_s.humid_array[hantei_s.time]) + "%となり、不快指数は『" + f_comment[hantei_s.n] + "』状態です。"
img1 = f_images[hantei_s.n]
home1 = "ちなみに部屋の温度は" + str(temphumid_h.h_temp) + "度、湿度は" + str(temphumid_h.h_humid) + "%となり、不快指数は『" + f_comment[hantei_h.h] + "』状態です。"
img2 = f_images[hantei_h.h]
fukai2 = "さらにちなみに現在の東京都千代田区の気温は" + str(fukai_t.temp_array_t[hantei_t.time]) + "度、湿度は" + str(fukai_t.humid_array_t[hantei_t.time]) + "%となり、不快指数は『" + f_comment[hantei_t.m] + "』状態です。"
img3 = f_images[hantei_t.m]

## FLASKの起動
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
# 不快指数と画像の読み込み
    return render_template("index.html", fukai1_value = fukai1, fukai2_value = fukai2, 
    img1_value = img1, img2_value = img2, img3_value = img3, home1_value = home1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

