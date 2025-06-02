from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialisierung
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gripper_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S1)

# Farbkodierung
OBJECT_COLOR = Color.RED       # Farbe des "Pakets"
TARGET_ZONE_COLOR = Color.BLUE # Farbe des Zielbereichs

# Geschwindigkeiten
SPEED = 100

# Greifarm-Funktionen
def close_gripper():
    gripper_motor.run_angle(200, -90)  # schließe den Greifarm
    wait(500)

def open_gripper():
    gripper_motor.run_angle(200, 90)   # öffne den Greifarm
    wait(500)

# Geradeaus fahren
def drive_forward(duration_ms):
    left_motor.run(SPEED)
    right_motor.run(SPEED)
    wait(duration_ms)
    left_motor.stop()
    right_motor.stop()

# Navigation zur Zielzone (über Farbsensor)
def navigate_to_target_zone():
    left_motor.run(SPEED)
    right_motor.run(SPEED)
    while True:
        if color_sensor.color() == TARGET_ZONE_COLOR:
            left_motor.stop()
            right_motor.stop()
            break
        wait(10)

# Hauptprogramm
def main():
    ev3.speaker.say("Starte Transport")

    open_gripper()

    # Zur Ablagestelle fahren
    drive_forward(2000)

    # Farbe des Objekts prüfen
    obj_color = color_sensor.color()
    if obj_color == OBJECT_COLOR:
        ev3.speaker.say("Richtiges Objekt")
        close_gripper()

        # Zur Zielzone fahren
        navigate_to_target_zone()

        # Objekt ablegen
        open_gripper()
        ev3.speaker.say("Abgelegt")
    else:
        ev3.speaker.say("Falsches Objekt")
        drive_forward(-1000)  # Rückwärts fahren, falls falsch

main()
