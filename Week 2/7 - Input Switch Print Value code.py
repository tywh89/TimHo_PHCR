# import  modudles and libraries
import board
import time
from digitalio import DigitalInOut, Direction

# declare varialbes and objects
switch = DigitalInOut(board.A1)
switch.direction = Direction.INPUT

# loop forever
while True:
    # print switch.value to the serial monitor
    print(switch.value)
    # pause a bit
    time.sleep(0.5)
