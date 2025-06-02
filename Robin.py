from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait


ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
middle_motor = Motor(Port.A)
gyro = GyroSensor(Port.S2, direction=Direction.CLOCKWISE)

def drive_forward(degrees_speed, target_degrees):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    left_motor.run(degrees_speed)
    right_motor.run(degrees_speed)
    
    while True:
        avg_angle = (abs(left_motor.angle()) + abs(right_motor.angle())) / 2
        if avg_angle >= target_degrees:
            break
        wait(10)
    
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    
    return avg_angle

def turn_180():
    gyro.reset_angle(0)
    left_motor.run(100)
    right_motor.run(-100)
    while gyro.angle() < 180:
        wait(10)
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

# Hauptprogramm
def main():
    # 1. Vorwärts fahren und Distanz speichern
    DISTANCE_DEGREES = 720 
    actual_distance = drive_forward(200, DISTANCE_DEGREES)

    # Objekt ablegen
    middle_motor.run_target(200, 90)
    wait(500)
    middle_motor.run_target(200, 0)

    turn_180()

    # Rückwärts fahren mit exakt der gleichen Distanz
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    left_motor.run(-200)
    right_motor.run(-200)
    
    while True:
        avg_angle = (abs(left_motor.angle()) + abs(right_motor.angle())) / 2
        if avg_angle >= actual_distance:
            break
        wait(10)
    
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

    # Fertig – zurück an Startposition
    ev3.speaker.beep()

main()
