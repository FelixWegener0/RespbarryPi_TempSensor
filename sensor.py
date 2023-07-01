import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT.DHT11
pin = 14
    
def getTemperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    sleep(1.5)

    if humidity is not None and temperature is not None:
        return temperature
    else:
        return 'Sensor Error'
    
def getHumidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    sleep(1.5)

    if humidity is not None and temperature is not None:
        return humidity
    else:
        return 'Sensor Error'