import sys
import signal
import os
import time
import Adafruit_DHT
from sys import exit

def signal_handler(signal, frame):
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 25

try:
    f = open('/opt/log/dht.csv', 'a+')
    if os.stat('/opt/log/dht.csv').st_size == 0:
            f.write('Timestamp,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    # convert the temperature to Fahrenheit.
    temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        f.write('{0},{1:0.1f},{2:0.1f}%\r\n'.format(time.strftime('%Y-%m-%d %H:%M'), temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(60)

exit()
