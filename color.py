from pybricks.parameters import Port, Color
from pybricks.ev3devices import ColorSensor

# Initialize the color sensor
color_sensor = ColorSensor(Port.S1)

def read_color(color_sensor: ColorSensor) -> str:
    """
    Reads the color detected by the color sensor and returns the color name as a string.

    Args:
        color_sensor (ColorSensor): The color sensor instance.

    Returns:
        str: The name of the detected color.
    """
    # Get the detected color from the sensor
    color = color_sensor.color()

    # Dictionary mapping color constants to their string names
    color_mapping = {
        Color.RED: "red",
        Color.GREEN: "green",
        Color.BLUE: "blue",
        Color.YELLOW: "yellow",
        Color.WHITE: "white",
        Color.BLACK: "black",
        Color.BROWN: "brown"
    }

    # Return the name of the color as a string
    return color_mapping.get(color, "unknown")

# Example usage
detected_color = read_color(color_sensor)
if detected_color == 'red':
    print('The red color has been detected')
else:
    print(f'The detected color is {detected_color}')