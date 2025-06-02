from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialisierung
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
sensor = ColorSensor(Port.S1)

# Zielzonenfarbe
TARGET_COLOR = Color.BLUE

# Geschwindigkeit
SPEED = 100

# Linienfolger mit einfacher Farbregel
def follow_line_to_color():
    while True:
        detected_color = sensor.color()

        # Wenn Zielzonenfarbe erkannt → stoppen
        if detected_color == TARGET_COLOR:
            left_motor.stop()
            right_motor.stop()
            ev3.speaker.say("Ziel erreicht")
            break

        # Linienfolger (sehr einfach)
        if detected_color == Color.BLACK:
            # Fahre geradeaus
            left_motor.run(SPEED)
            right_motor.run(SPEED)
        else:
            # Drehe leicht nach links, um Linie zu finden
            left_motor.run(SPEED // 2)
            right_motor.run(SPEED)

        wait(10)
