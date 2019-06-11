#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.led import Leds
from time import sleep


# Connect ultrasonic and touch sensors to any sensor port
us = UltrasonicSensor()
ts = TouchSensor()
leds = Leds()

leds.all_off() # stop the LEDs flashing

# Main Loop
while not ts.is_pressed:
    if us.distance_centimeters < 40:
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
    else:
        leds.set_color('LEFT',  'GREEN')
        leds.set_color('RIGHT', 'GREEN')

    sleep (0.01) # Give the CPU a rest

