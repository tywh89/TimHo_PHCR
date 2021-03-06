# import moduels and libraries
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# declare neopixel with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)


# declare digital input object on pin D7, slideswitch
switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# declare digital input object on pin D7, slideswitch
buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonA_pre = buttonA.value

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN
buttonB_pre = buttonB.value

# create a color variable and fill the pixels with the color
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = WHITE
pixels.fill(color)

# loop forever
while True:
    pass
    if switch.value:
        pixels.fill(color)

    else:
        pixels.fill(0)

    if buttonA.value != buttonA_pre:
        buttonA_pre = buttonA.value
        if buttonA.value:
            color = BLUE
            print(color)

    if buttonB.value != buttonB_pre:
        buttonB_pre = buttonB.value
        if buttonB.value:
            color = RED
            print(color)

    if buttonA_pre and buttonB_pre:
        color = GREEN


# rest
    time.sleep(0.1)


