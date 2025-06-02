#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialisierung
ev3 = EV3Brick()

medium_motor = Motor(Port.A)  # Greifarm (Hebel)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)  # Farbsensor vorne

# Reset der Motoren
medium_motor.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

# DriveBase einrichten
wheel_diameter = 56  # mm
axle_track = 114     # mm
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Gesuchte Farben definieren
OBJECT_COLOR = Color.RED        # Objekt, das gegriffen werden soll
TARGET_COLOR = Color.BLUE       # Zielzone

# Startmeldung
ev3.speaker.say("Suche Objekt")

# 1. Rückwärts fahren (z. B. zum Objekt hin)
drive_base.straight(-100)

# 2. Leichte Drehung nach rechts
drive_base.turn(20)

# 3. Farbe prüfen
if color_sensor.color() == OBJECT_COLOR:
    ev3.speaker.say("Objekt erkannt")

    # 4. Hebel (Greifarm) leicht nach unten – z. B. um Objekt zu greifen
    medium_motor.run_target(
        speed=200,
        target_angle=-20,
        then=Stop.HOLD,
        wait=True
    )

    # 5. Vorwärts zur Zielzone
    drive_base.straight(150)

    # 6. Zielzone erkennen
    ev3.speaker.say("Suche Zielzone")
    while True:
        if color_sensor.color() == TARGET_COLOR:
            drive_base.stop()
            ev3.speaker.say("Zielzone erkannt")
            break
        drive_base.straight(20)
        wait(100)

    # 7. Objekt ablegen (Greifarm nach oben)
    medium_motor.run_target(
        speed=200,
        target_angle=30,  # z. B. wieder hoch
        then=Stop.HOLD,
        wait=True
    )

    ev3.speaker.say("Transport abgeschlossen")

else:
    ev3.speaker.say("Falsches Objekt")
    drive_base.straight(100)  # Zurückfahren, wenn falsches Objekt

