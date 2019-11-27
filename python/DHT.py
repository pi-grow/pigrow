#!/usr/bin/python

import sys
import signal
import time
import Adafruit_DHT
from sys import exit

def signal_handler(signal, frame):
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./DHT.py 22 18 - Read from an DHT22 connected to GPIO pin 18')
    sys.exit(1)

while True:
    try:
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # convert the temperature to Fahrenheit.
        temperature = temperature * 9/5.0 + 32
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    # Poll every 2 Seconds
    time.sleep(2.0)
    # Ctrl-C to Exit

