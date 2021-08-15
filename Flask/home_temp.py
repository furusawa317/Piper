## ラズパイ
# 家のラズパイからMosquito経由で温度情報を受信し、home.txtに蓄積している
# 下記でhome.txtを読みこみ、リストに全て投入し、最新情報だけをhome_temp変数に代入
f = open('C:\home.txt', 'r')
datalist = f.readlines()
home_temp = datalist[-1]

#　改行の削除
home_temp = home_temp.replace( '\n' , '' )

#print(home_temp)