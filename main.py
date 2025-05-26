from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
 
sensor = ColorSensor(INPUT_1)
 
farbe = sensor.color
 
if farbe == 1:
    print("Farbe erkannt: Schwarz")
elif farbe == 2:
    print("Farbe erkannt: Blau")
elif farbe == 3:
    print("Farbe erkannt: Grün")
elif farbe == 4:
    print("Farbe erkannt: Gelb")
elif farbe == 5:
    print("Farbe erkannt: Rot")
elif farbe == 6:
    print("Farbe erkannt: Weiß")
elif farbe == 7:
    print("Farbe erkannt: Braun")
else:
    print("Keine Farbe erkannt")