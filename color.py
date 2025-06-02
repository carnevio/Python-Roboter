from pybricks.parameters import Port, Color
from pybricks.ev3devices import ColorSensor
color_sensor = ColorSensor(Port.S1)


def read_color(colorsensor: ColorSensor) -> str:
    # Get the detected color from the sensor
    # color = color_sensor.color()

    # Return the name of the color as a string
    if color == Color.RED:
        return "red"
    elif color == Color.GREEN:
        return "green"
    elif color == Color.BLUE:
        return "blue"
    elif color == Color.YELLOW:
        return "yellow"
    elif color == Color.WHITE:
        return "white"
    elif color == Color.BLACK:
        return "black"
    elif color == Color.BROWN:
        return "brown"
    else:
        return "unknown"

if read_color(color_sensor) == 'red':
    print('the red color has been detected')