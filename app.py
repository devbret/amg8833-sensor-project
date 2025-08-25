import time
import board
import busio
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)

try:
    sensor = adafruit_amg88xx.AMG88XX(i2c)
    print("AMG8833 detected!")

    while True:
        pixels = sensor.pixels
        for row in pixels:
            print(["{0:.1f}".format(temp) for temp in row])
        print("\n")
        time.sleep(1)

except Exception as e:
    print("Could not talk to AMG8833:", e)