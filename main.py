import Adafruit_DHT
from time import sleep
sensor = Adafruit_DHT.DHT11

pin = 14
print("[press ctrl+c to end the script]") 
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor,
        pin)
        sleep(1.5)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C Humidity={1:0.1f}%"
            .format(temperature, humidity))
        else:
            print("Failed to get reading. Try again!")
except KeyboardInterrupt:
    print("Script end!")