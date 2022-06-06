import time
from adafruit_blinka.agnostic import board_id
import busio
import adafruit_adxl34x

i2c = busio.I2C(SCL, SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)