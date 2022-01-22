import os
import paho.mqtt.client as mqtt

client = mqtt.Client(protocol=mqtt.MQTTv311)
HOST = os.environ['HOST_ENDPOINT']  # AWS IoT Endpoint
PORT = 8883  # mqtts port
CACERT = os.environ['CACERT']  # root ca
CLIENTCERT = os.environ['CLIENTCERT']  # certificate
CLIENTKEY = os.environ['CLIENTKEY']  # private key
TOPIC_MOTION = os.environ['TOPIC_MOTION']  # topic
TOPIC_DUST = os.environ['TOPIC_DUST']  # topic

MOTION_PIN = 21
DUST_PIN =15

SENSOR_NO = int(os.environ['SENSOR_NO'])
