#!/usr/bin/env pybricks-micropython
 
from pybricks.hubs import EV3Brick

from pybricks.ev3devices import Motor

from pybricks.parameters import Port, Stop

from pybricks.robotics import DriveBase
 
# Initialisierung

ev3 = EV3Brick()
 
medium_motor = Motor(Port.A)  # Aktor

left_motor   = Motor(Port.B)

right_motor  = Motor(Port.C)
 
medium_motor.reset_angle(0)

left_motor.reset_angle(0)

right_motor.reset_angle(0)
 
# DriveBase einrichten

wheel_diameter = 56  # mm

axle_track = 114     # mm

drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
 
# 1. 10 cm (100 mm) rückwärts

drive_base.straight(-100)
 
# 2. 15° nach rechts drehen (im Uhrzeigersinn)

drive_base.turn(20)
 
# 3. Aktor 15° nach rechts drehen

medium_motor.run_target(

    speed=200,

    target_angle=-20,

    then=Stop.HOLD,

    wait=True

)
 
# 4. 15 cm (150 mm) vorwärts

drive_base.straight(150)
 
# 5. Aktor nochmals 15° nach rechts drehen (insgesamt 30°)

medium_motor.run_target(

    speed=200,

    target_angle=30,  # Weil er schon bei 15° ist

    then=Stop.HOLD,

    wait=True

)

 

 