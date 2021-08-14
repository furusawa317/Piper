import requests
import bs4

URL = 'https://tenki.jp/forecast/1/2/1400/1108/1hour.html'

r = requests.get(URL)
s = bs4.BeautifulSoup(r.text, 'html.parser')

#リストの作成
list_temp= []

#入れ子の要素取得（取得要素の絞り込み）
for j in s.find_all('tr' , class_ ='temperature'):
    for i in j.find_all("span"):
        list_temp.append(i.string)

temp=[]
for i in range(0,24,1):
    print(list_temp[i])
    temp.append(list_temp[i])