import boto3
import re

# S3から部屋の温度・湿度データを取得
s3 = boto3.resource('s3')
bucket = s3.Bucket('furusawatest')
bucket.download_file('home.txt', 'D:\home.txt')

# ファイルの読み込み
homefile = open(r'D:\home.txt', 'r')
data = homefile.read()
homefile.close()

# 不要な情報を削除し、温度と湿度情報をfloatに変換
a = data[12:]
b = a[:-25]

c = re.findall("(?<=\().+?(?=\))", b)

d = c[0][1:][:-1]
e = c[1][1:][:-1]

h_humid = float(c[0][1:][:-1])
h_temp = float(c[1][1:][:-1])

print(h_humid, h_temp)