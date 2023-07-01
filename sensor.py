import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT.DHT11
pin = 14

def getInfo(): 
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    sleep(1.5)

    if humidity is not None and temperature is not None:
        return { temperature, humidity }
    else:
        return { 0, 0 }