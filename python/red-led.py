#!/usr/bin/python3
import sys
import signal
import time
import datetime
import RPi.GPIO as GPIO
from sys import exit

GPIO.setwarnings(False)

def signal_handler(signal, frame):
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main ():
    LED =18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)

    while (True):
        now = datetime.datetime.now()
        todayon = now.replace(hour = 2, minute=45, second =0, microsecond =0)
        todayoff = now.replace(hour = 23, minute=15, second =0, microsecond =0)
        turnon = now>todayon and now<todayoff
        turnoff = now>todayoff

        if(turnon == True):
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)

        if(turnoff == True):
                GPIO.output(LED, GPIO.HIGH)

if __name__ == '__main__':
    main()
exit()
