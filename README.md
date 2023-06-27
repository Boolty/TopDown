# Projekt-Dokumentation: Wasserfall Modell

Bei der vorliegenden Projekt-Dokumentation handelt es sich um ein Wasserfall Modell, das den Code für das Spiel "TopDown" beschreibt, das mit der Python-Bibliothek Pygame entwickelt wurde. Das Spiel bietet ein Menü mit verschiedenen Optionen, darunter "Start", "Einstellungen" und "Schließen". Nach Auswahl der Optionen können verschiedene Aktionen ausgeführt werden, wie das Starten des Spiels oder das Anpassen der Einstellungen.

## WhiteBox Test
Auf der Seite am Schluss.

## Systemvoraussetzungen:
- MacOS
- Windows

## Verwendete Bibliotheken:
- pygame
- shutil
- os
- sys
- math
- threading

## Klassen und Funktionen:
### Klasse Game:
- `__init__(self)`: Der Konstruktor der Klasse initialisiert das Spiel. Es wird eine Pygame-Instanz erstellt, ein Fenster mit der angegebenen Breite und Höhe geöffnet, der Titel des Fensters festgelegt und der Hintergrund geladen. Außerdem werden die erforderlichen Attribute initialisiert.
- `show_win_animation(screen)`: Eine statische Methode zum Anzeigen einer Gewinnanimation. Es wird ein schwarzer Hintergrund mit dem Text "Gewonnen!" und einem weißen Text auf dem Bildschirm angezeigt. Die Animation wird für 2 Sekunden angezeigt.
- `run(self)`: Die Hauptmethode des Spiels. Sie enthält die Hauptschleife, in der Ereignisse behandelt, der Hintergrund gezeichnet, das Level aktualisiert und der Bildschirm aktualisiert wird.

## Hauptprogramm:
Das Hauptprogramm enthält die Initialisierung von Pygame, das Festlegen der Fenstergröße, die Verwendung der Schriftart, die Definition der Menüoptionen und die Hauptschleife. In der Hauptschleife werden Ereignisse behandelt, die Auswahl im Menü geändert und die entsprechenden Aktionen ausgeführt.

## Einstellungen:
Die Einstellungen des Spiels werden in einer separaten Datei mit dem Namen "settings.py" definiert. Die Einstellungen umfassen die Breite und Höhe des Fensters, die Bildwiederholrate (FPS) sowie verschiedene Einstellungen für den Spieler und den Feind.

## Funktionsweise:
Das Spiel "TopDown" bietet ein Menü mit verschiedenen Optionen. Durch Drücken der Pfeiltasten nach oben und unten kann der Benutzer die Option auswählen, und durch Drücken der Eingabetaste kann die ausgewählte Option ausgeführt werden.
- Wenn die Option "Start" ausgewählt wird, wird das Spiel initialisiert und die `run()`-Methode der Game-Klasse aufgerufen, um das Spiel zu starten.
- Wenn die Option "Einstellungen" ausgewählt wird, werden die aktuellen Einstellungen angezeigt und der Benutzer kann sie ändern. Die geänderten Einstellungen werden in der Datei "settings.py" gespeichert.
- Wenn die Option "Schließen" ausgewählt wird, wird das Spiel beendet.

## Anpassung der Einstellungen:
Die Einstellungen können im Menü "Einstellungen" geändert werden. Der Benutzer kann eine Zahl von 0 bis 11 eingeben, um die gewünschte Einstellung auszuwählen. Nach der Auswahl.
