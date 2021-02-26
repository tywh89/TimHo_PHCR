# import modules
import time
import board
import pulseio

# make a led object with pulseio.PWMOut on pin board.A1
led = pulseio.PWMOut(board.A1, duty_cycle-0)

"""
pulseio.PWMOut creates a PWMOut object with the name led

you can set the duty_cycle with the property led.duty_cycle

led.duty_cycle accepts a 16-bit interger value from 0 - 65535
"""

# loop forver
while True:
    # set on duty_cycle
    led.duty_cycle = 10000
    time,sleep(0.5)

    # set a different duty_cycle
    led.duty_cycle = 108
    time.sleep(0.5)