# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# loop forever
while True:
    # turn the led on 1
    led.value = True
    time.sleep(.125)
    # turn the led off 1
    led.value = False
    time.sleep(.125)


