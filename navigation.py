# Voraussetzungen:
# - Gyrosensor an PORT 2
# - Linker Motor an PORT B
# - Rechter Motor an PORT C

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_2
from time import sleep

# Motorsteuerung initialisieren (linker Motor = B, rechter Motor = C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# Gyrosensor initialisieren (an Port 2)
gyro = GyroSensor(INPUT_2)
gyro.reset()  # Wichtig: Nullstellung setzen vor dem Start

def drive_straight(duration=2, speed=30):
    """
    Fährt geradeaus für eine bestimmte Zeit.
    :param duration: Fahrzeit in Sekunden
    :param speed: Geschwindigkeit der Motoren (0–100)
    """
    tank_drive.on(speed, speed)
    sleep(duration)
    tank_drive.off()

def turn(degrees, speed=15):
    """
    Dreht den Roboter um die gewünschte Gradzahl mithilfe des Gyrosensors.
    Positive Werte = Rechtsdrehung, Negative = Linksdrehung.
    :param degrees: Zielwinkel in Grad
    :param speed: Drehgeschwindigkeit
    """
    gyro.reset()
    if degrees > 0:
        tank_drive.on(speed, -speed)  # Rechtsdrehung
        while gyro.angle < degrees:
            sleep(0.01)
    else:
        tank_drive.on(-speed, speed)  # Linksdrehung
        while gyro.angle > degrees:
            sleep(0.01)
    tank_drive.off()

# 🧭 Hauptprogramm: Navigation zur Ablagestelle
# Beispielablauf: Vorfahren → 90° Drehung → Weiterfahren

#Functioncalls diese müssen dann mit der Farberkennung und der Objekterkennung erweitert werden
drive_straight(2, 40)   # 2 Sekunden geradeaus
turn(90)                # 90° nach rechts drehen
drive_straight(1.5, 40) # 1.5 Sekunden weiterfahren
