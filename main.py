#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialisierung
ev3 = EV3Brick()

# Motoren
medium_motor = Motor(Port.A)  # Greifarm (Hebel)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Farbsensor vorne
color_sensor = ColorSensor(Port.S4)

# Motor-Reset
medium_motor.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

# DriveBase einrichten
wheel_diameter = 56  # mm
axle_track = 114     # mm
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Farben definieren
OBJECT_COLOR = Color.GREEN
TARGET_COLOR = Color.BLUE

# Start
ev3.speaker.say("Suche Objekt")

# 1. 10 cm rückwärts
drive_base.straight(-100)

# 2. 15° nach rechts
drive_base.turn(20)

# 3. Farbe prüfen
if color_sensor.color() == OBJECT_COLOR:
    ev3.speaker.say("Objekt erkannt")

    # 4. Greifarm leicht absenken
    medium_motor.run_target(
        speed=200,
        target_angle=-56,
        then=Stop.HOLD,
        wait=True
    )

    # 5. 15 cm vorwärts
    drive_base.straight(100)

    # 6. Greifarm weiter absenken auf 30°
    medium_motor.run_target(
        speed=200,
        target_angle=-30,
        then=Stop.HOLD,
        wait=True
    )

    # 7. Zielzone finden
    ev3.speaker.say("Suche Zielzone")
    while True:
        if color_sensor.color() == TARGET_COLOR:
            drive_base.stop()
            ev3.speaker.say("Zielzone erkannt")
            break
        drive_base.straight(20)
        wait(100)

    # 8. Objekt ablegen (Greifarm wieder hoch)
    medium_motor.run_target(
        speed=200,
        target_angle=60,
        then=Stop.HOLD,
        wait=True
    )

    ev3.speaker.say("Transport finished")

else:
    ev3.speaker.say("Falsches Objekt")
    drive_base.straight(100)  # Zurückfahren
