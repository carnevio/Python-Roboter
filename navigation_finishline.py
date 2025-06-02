from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

medium_motor = Motor(Port.A)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

medium_motor.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

heel_diameter = 56  
axle_track = 114     
drive_base = DriveBase(left_motor, right_motor,
                       wheel_diameter, axle_track)
