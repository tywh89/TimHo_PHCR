# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# variables to control sleep time for blinking
onTime = .25
offTime = 0.125
onTime2 = 1
offTime2 = 2


# loop forever
while True:
    # turn the led on 1
    led.value = True
    time.sleep(onTime)
    # turn the led off 1
    led.value = False
    time.sleep(offTime)
    # turn the led on 2
    led.value = True
    time.sleep(onTime)
    # turn the led off 2
    led.value = False
    time.sleep(offTime)
    # turn the led on 3
    led.value = True
    time.sleep(onTime)
    # turn the led off 3
    led.value = False
    time.sleep(offTime)

    # turn the led on 4
    led.value = True
    time.sleep(onTime2)
    # turn the led off 4
    led.value = False
    time.sleep(offTime)
    # turn the led on 5
    led.value = True
    time.sleep(onTime2)
    # turn the led off 5
    led.value = False
    time.sleep(offTime)
    # turn the led on 6
    led.value = True
    time.sleep(onTime2)
    # turn the led off 6
    led.value = False
    time.sleep(offTime)

    # turn the led on 7
    led.value = True
    time.sleep(onTime)
    # turn the led off 7
    led.value = False
    time.sleep(offTime)
    # turn the led on 8
    led.value = True
    time.sleep(onTime)
    # turn the led off 8
    led.value = False
    time.sleep(offTime)
    # turn the led on 9
    led.value = True
    time.sleep(onTime)
    # turn the led off 9
    led.value = False
    time.sleep(offTime)

    # turn the led off 10
    led.value = False
    time.sleep(offTime2)


