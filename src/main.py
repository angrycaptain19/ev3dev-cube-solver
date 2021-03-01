#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

ir = InfraredSensor(INPUT_2)
leds = Leds()
sound = Sound()
rotatingPlatform = LargeMotor(OUTPUT_B)
arm = LargeMotor(OUTPUT_A)

count = 0

sound.beep()





while count < 150:
    distance = ir.value()

    if distance <= 20 and distance >= 14:
        count = count + 1

    sleep(0.01)

sound.speak('Starting rotation')

arm.position = 0
arm.on_for_degrees(SpeedPercent(20), 90)
sleep(0.1)

rotatingPlatform.position = 0
rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

arm.on_for_degrees(SpeedPercent(20), 90)
sleep(0.5)
arm.on_for_degrees(SpeedPercent(20), -90)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

rotatingPlatform.on_for_degrees(SpeedPercent(75), 300)
rotatingPlatform.on_for_degrees(SpeedPercent(75), -30)

sleep(0.1)
arm.on_for_degrees(SpeedPercent(20), -90)
sound.beep()
