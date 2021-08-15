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

#不要な要素を削除し、tempりストに入れ直す
temp = []
for i in range(0,24,1):
    temp.append(list_temp[i])

## 湿度の取り込み
#湿度リストの作成
list_humid= []

#入れ子の要素取得（取得要素の絞り込み）
for j in s.find_all('tr' , class_ ='humidity'):
    for i in j.find_all("span"):
        list_humid.append(i.string)

#不要な要素を削除し、humidリストに入れ直す
humid=[]
for i in range(1,25,1):
    humid.append(list_humid[i])

#print(temp)
#print(humid)