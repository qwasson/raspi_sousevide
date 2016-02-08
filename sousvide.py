import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

from libbcm import setupSocket
from libbcm import switchSocket

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK = 11
CS  = 9
DO  = 10
sensor = MAX31855.MAX31855(CLK, CS, DO)

setupSocket()

targetTemp = 30

tempRange = 1

heating = False;

# Initial read
temp = sensor.readTempC()
print 'Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp))

heating = temp < (targetTemp + tempRange)

if(heating):
    print 'initially heating'
else:
    print 'initially not heating'

switchSocket(heating, 1)

# Loop printing measurements every second.
print 'Press Ctrl-C to quit.'
while True:

    temp = sensor.readTempC()
    internal = sensor.readInternalC()

    if(heating and temp >= (targetTemp + tempRange)):
        heating = False        
        print 'stopping heating'
    elif(not heating and temp < (targetTemp - tempRange)):
        heating = True
        print 'starting heating'
    

    switchSocket(heating, 1)    
        
    print 'Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp))

    time.sleep(1.0)
