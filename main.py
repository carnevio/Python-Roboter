#!/usr/bin/env pybricks-micropython
# Programm 2: Display-Ausgabe und Sound
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.media.ev3dev import SoundFile   # enthält u. a. SoundFile.HELLO

ev3 = EV3Brick()

# Begrüssung anzeigen und einen Ton abspielen
ev3.screen.clear()                   # Bildschirm löschen
ev3.screen.print("Hallo, EV3!")       # Text auf dem Display anzeigen
ev3.screen.print("AMK legge eier")
ev3.speaker.play_file(SoundFile.HELLO)        # Sounddatei "HELLO" abspielen

# Warten, bis Mitte-Taste gedrückt wird
while Button.CENTER not in ev3.buttons.pressed():
    pass

# Rückmeldung
ev3.screen.clear()
ev3.screen.print("Taste erkannt!")
ev3.speaker.beep()
