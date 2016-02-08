#import the required modules
import RPi.GPIO as GPIO
import time

#  BOARD    BCM
#    3      0/2
#    5      1/3
#    7       4
#    8      14
#   10      15
#   11      17
#   12      18
#   13      27
#   15      22
#   16      23
#   18      24
#   19      10
#   21       9
#   22      25
#   23      11
#   24       8
#   16       7

def setupSocket():
    GPIO.setmode(GPIO.BCM) # set the pins numbering mode

    GPIO.setup(17, GPIO.OUT) # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    
    GPIO.setup(24, GPIO.OUT)# Select the signal to select ASK/FSK
    
    GPIO.setup(25, GPIO.OUT)# Select the signal used to enable/disable the modulator
    
    GPIO.output (25, False) # Disable the modulator by setting CE pin lo
    
    GPIO.output (24, False) # Set the modulator to ASK for On Off Keying  by setting MODSEL pin lo
    
    GPIO.output (17, False) # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output (22, False)
    GPIO.output (23, False)
    GPIO.output (27, False)

def switchSocket(on, sockId):
    
    # Set K0-K3
    k0 = ((7 - (sockId - 1)) & 1) != 0
    k1 = ((7 - (sockId - 1)) & 2) != 0
    k2 = ((7 - (sockId - 1)) & 4) != 0
    k3 = on

    GPIO.output (17, k0)
    GPIO.output (22, k1)
    GPIO.output (23, k2)
    GPIO.output (27, k3)
    # let it settle, encoder requires this
    time.sleep(0.1) 
    # Enable the modulator
    GPIO.output (25, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (25, False)

def switchAll(on):
    switchSocket(not on, 5)

def demo():
    setupSocket()
    try:
        # We will just loop round switching the units on and off
        while True:
            raw_input('hit return key to send socket' + str(1) + ' ' + str() + ' code')
            switchSocket(True, 1)

            raw_input('hit return key to send socket' + str(sockId) + ' ' + str(on) + ' code')
            switchSocket(False, 1)

            switchSocket(True, 2)

            switchSocket(False, 2)

            switchAll(True)

            switchAll(False)

    # Clean up the GPIOs for next time
    except KeyboardInterrupt:
        GPIO.cleanup()

