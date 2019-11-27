#!/usr/bin/python

import sys
import signal
import time
import datetime
import Adafruit_DHT
from sys import exit

def signal_handler(signal, frame):
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

currentDT = datetime.datetime.now()


try:
    humidity, temperature = Adafruit_DHT.read_retry(11, 25)
    temperature = temperature * 9/5.0 + 32
    #
    with open('/opt/log/dht.csv', 'a+') as f:
        f.write(currentDT.strftime("%Y-%m-%d %H:%M:%S"))
        f.write(",")
        f.write('Temp={0:0.1f}*'.format(temperature))
        f.write("\n")

except RuntimeError as error:
    print(error.args[0])

exit()
