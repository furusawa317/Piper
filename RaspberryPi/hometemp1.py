# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# 参考： https://aws.amazon.com/jp/premiumsupport/knowledge-center/iot-core-publish-mqtt-messages-python/

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "ao1neorh0qc14-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "furusawa_20210817"
PATH_TO_CERT = "/home/pi/dummy_client/certs/61aabd8e8a-certificate.pem.crt"
PATH_TO_KEY = "/home/pi/dummy_client/certs/61aabd8e8a-private.pem.key"
PATH_TO_ROOT = "/home/pi/dummy_client/certs/AmazonRootCA1.pem"
MESSAGE = "Hello World"
TOPIC = "data/furusawa_20210817"
RANGE = 1

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERT,
            pri_key_filepath=PATH_TO_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_ROOT,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")

import datetime
dt_now = datetime.datetime.now()
now_time = dt_now.isoformat()
print(now_time)

##
import RPi.GPIO as GPIO
import dht11
import time
from datetime import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

module = dht11.DHT11(pin=18)

while True:
    result = module.read()
    if result.is_valid():
        break
    time.sleep(1)
temp=result.temperature
humid=result.humidity


## MQQTでのメッセージ送信
message = {"DEVICE_NAME": "furusawa_20210817",
  "TIMESTAMP": now_time,
  "TEMPERATURE": temp,
  "HUMIDITY": humid
   }

print(message)

mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)

# Publish message to server desired number of times.
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()