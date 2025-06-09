#!/usr/bin/env pybricks-micropython
#Rafaeal, Sven, Lukas, Robin, Nevio


#All diese Bibliotheken werden geladen
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


ev3 = EV3Brick()

#Diese Ports werden für die Motoren und den Farbsensor verwendet
medium_motor = Motor(Port.A)  
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


color_sensor = ColorSensor(Port.S4)


medium_motor.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)


wheel_diameter = 56  
axle_track = 114     
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


OBJECT_COLOR = Color.GREEN
TARGET_COLOR = Color.BLUE


ev3.speaker.say("Suche Objekt")


drive_base.straight(-100)


drive_base.turn(20)

if color_sensor.color() == OBJECT_COLOR:
    ev3.speaker.say("Objekt erkannt")


    medium_motor.run_target(
        speed=200,
        target_angle=-56,
        then=Stop.HOLD,
        wait=True
    )


    drive_base.straight(100)


    medium_motor.run_target(
        speed=200,
        target_angle=-30,
        then=Stop.HOLD,
        wait=True
    )

    ev3.speaker.say("Suche Zielzone")
    while True:
        if color_sensor.color() == TARGET_COLOR:
            drive_base.stop()
            ev3.speaker.say("Zielzone erkannt")
            break
        drive_base.straight(20)
        wait(100)

    
    medium_motor.run_target(
        speed=200,
        target_angle=60,
        then=Stop.HOLD,
        wait=True
    )

    ev3.speaker.say("Transport finished")

else:
    ev3.speaker.say("Falsches Objekt")
    drive_base.straight(100)  



#Dieser Code steuert einen EV3 Roboter, der ein Objekt erkennt , dies aufliest, es zu einer Zielzone transportiert und bei der Zielsone wieder absetz.

#Wir haben KI gebraucht um das Projekt in 5 Features zu unterteilen damit jeder ein Feature machen konnte. Zusätzlich haben wir vereinzeilt KI Tools benutzt um den Code zu schreiben, aber den grössten Teil anhand der beispiel Codes von Moodle

