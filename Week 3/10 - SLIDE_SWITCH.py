# import  modudles and libraries
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# declare varialbes and objects
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT


# declare an onboard SLIDE_SWITCH with Pull.UP
button = DigitalInOut(board.SLIDE_SWITCH)
button.direction = Direction.INPUT
button.pull = Pull.UP

# loop forever
while True:

    # read and print the button value
    print(button.value)

    # set led value to the button value
    led.value = button.value

    # sleep so the serial monitor doesn't crash!
    time.sleep(0.125)
    time.sleep(0.125)
