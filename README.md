# Transport- und Sortierroboter mit LEGO EV3

In diesem Repository entwickeln wir einen Transport- und Sortierroboter auf Basis des LEGO Mindstorms EV3.

## Projektbeschreibung

Ziel des Projekts ist es, einen autonomen Roboter zu bauen, der Objekte transportieren und sortieren kann. Die Programmierung erfolgt mit [MicroPython](https://micropython.org/) auf dem EV3-System.

## Technologien & Materialien

- LEGO Mindstorms EV3
- MicroPython
- Sensoren (z. B. Farbsensor, Ultraschallsensor)
- Motoren und EV3 Brick

## Voraussetzungen

- EV3 Brick mit installierter MicroPython-Firmware
- Entwicklungsumgebung wie Visual Studio Code
- USB- oder WLAN-Verbindung zum Roboter

## Autor:innen

-Hertling Rafael

## Lizenz

Dieses Projekt steht unter der S-INA24bl Mathe Lizenz Gruppe.

## Aufgabenverteilung
🔧 Aufteilung in 5 Teilfeatures
🔹 1. Navigation zur Ablagestelle (Startposition → Objekt)(Rafael)
Zuständig für: Grundnavigation mit Gyro/Encoder oder Linienfolge

Aufgabe: Der Roboter fährt selbstständig zur definierten Ablagestelle, wo sich das Objekt befindet.

Technik: Linienfolger oder einfache Geradeausfahrt mit Zeit/Encoder + Drehung

🔹 2. Farberkennung am Objekt (Lukas)
Zuständig für: Farbsensor-Logik

Aufgabe: Mit dem Farbsensor wird geprüft, ob das Objekt die gewünschte Farbe (z.B. Rot = „Paket“) hat.

Technik: Wenn die Farbe stimmt, wird Signal gegeben → weiter zum Greifen; sonst evtl. Abbruch oder Suche nach anderem Objekt (optional)

🔹 3. Greifmechanismus (Mittlerer Motor)(Sven)
Zuständig für: Objektaufnahme und -abgabe

Aufgabe: Mittlerer Motor steuert Greifarm oder Hebegabel.

Greifarm runter

Objekt aufnehmen

Greifarm hoch

Technik: Exakte Winkelsteuerung des Motors

🔹 4. Navigation zur Zielzone (Objekt → Zielort) (Nevio)
Zuständig für: Navigation mit Referenz (z.B. Bodenfarbe, bestimmte Strecke, Linie)

Aufgabe: Der Roboter fährt zur Zielzone, wo das Objekt abgeliefert werden soll.

Technik: Linienfolger, Farberkennung der Zielzone oder koordinatenbasierte Navigation

🔹 5. Objekt ablegen und zurückkehren (Robin)
Zuständig für: Abgabe durch Motorsteuerung + Rückfahrt

Aufgabe:

Objekt ablegen (Mittlerer Motor senken)

ggf. Rückkehr zur Startposition oder bereit für nächsten Auftrag

Technik: Wieder Mittlerer Motor steuern + einfache Navigation

