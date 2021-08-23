# 参考、引用元
# https://www.tantan-biyori.info/blog/2018/11/aws-dynamo.html
# https://recipe.kc-cloud.jp/archives/10058

import boto3
dynamodb = boto3.resource('dynamodb')
from datetime import datetime
print('Loading function')
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    table_name = "test"
    primary_key = {"deviceid": event["deviceid"]}
    dynamotable = dynamodb.Table(table_name)
    res = dynamotable.get_item(Key=primary_key)
    item = str(res["Item"])

    bucket = 'furusawatest'
    key = 'home.txt'
    file_contents = item 
    obj = s3.Object(bucket,key)
    obj.put( Body=file_contents )

    return item