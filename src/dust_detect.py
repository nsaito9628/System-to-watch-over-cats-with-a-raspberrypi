#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import sys
from awsMQTTconnect import Com, Pub
from sensing import Sensor


senser = Sensor()
com = Com()
pub = Pub()


def loop():
    sub_t_countdust = 0
    dust_count = 0

    while True:
        dust_count = dust_count + senser.get_pm25()

        #print("{:.2f}".format(dust_count))

        bool, sub_t_countdust = pub.publish_dust(sub_t_countdust, dust_count)

        if bool == True: dust_count = 0

        time.sleep(0.025)


if __name__ == '__main__':
    try:
        time.sleep(90)

        #wifi connection confirmation and MQTT connection
        com.get_ssid()
        com.aws_connect()

        #Main loop execution
        loop()

    except KeyboardInterrupt:
        sys.exit()
