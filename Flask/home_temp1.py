## ラズパイ
# 家のラズパイからAWS IoTからS3に保存
# その後、本プログラムでS3から受信し、辞書形式に保存

import boto3
import json
from collections import OrderedDict
import pprint

s3 = boto3.resource('s3')

bucket = s3.Bucket('furusawatest')
bucket.download_file('home_temp.txt', 'D:\home_temp.txt')

# homefileとして、その後dataにstrで保存
homefile = open('D:\home_temp.txt', 'r', encoding='UTF-8')
data = homefile.read()
homefile.close()
#print(data)

# strから辞書形式に変換
home_temp = json.loads(data)
pprint.pprint(home_temp, width=40)

#print(home_temp)
print(home_temp["TEMPERATURE"])
print(home_temp["HUMIDITY"])