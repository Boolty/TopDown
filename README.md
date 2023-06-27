Projekt-Dokumentation: Wasserfall Modell
Bei dem  vorliegende Projekt-Dokumentation handelt es sich um ein Wasserfall Modell das beschreibt den Code für das Spiel "TopDown", das mit der Python-Bibliothek Pygame entwickelt wurde. Das Spiel bietet ein Menü mit verschiedenen Optionen, darunter "Start", "Einstellungen" und "Schließen". Nach Auswahl der Optionen können verschiedene Aktionen ausgeführt werden, wie das Starten des Spiels oder das Anpassen der Einstellungen.
Kosten:
á 12 Stunden 5,60€
Gesamte kosten : 87,60€

WhiteBox Test:
Auf der Seite am Schluss. 

SystemvoraussetzungenÄ:
    • MacOS
    • Windows
      
Verwendete Bibliotheken:
    • pygame
    • shutil
    • os
    • sys
    • math
    • threading
Klassen und Funktionen:
Klasse Game:
    • __init__(self): Der Konstruktor der Klasse initialisiert das Spiel. Es wird eine Pygame-Instanz erstellt, ein Fenster mit der angegebenen Breite und Höhe geöffnet, der Titel des Fensters festgelegt und der Hintergrund geladen. Außerdem werden die erforderlichen Attribute initialisiert.
    • show_win_animation(screen): Eine statische Methode zum Anzeigen einer Gewinnanimation. Es wird ein schwarzer Hintergrund mit dem Text "Gewonnen!" und einem weißen Text auf dem Bildschirm angezeigt. Die Animation wird für 2 Sekunden angezeigt.
    • run(self): Die Hauptmethode des Spiels. Sie enthält die Hauptschleife, in der Ereignisse behandelt, der Hintergrund gezeichnet, das Level aktualisiert und der Bildschirm aktualisiert wird.


Hauptprogramm:
Das Hauptprogramm enthält die Initialisierung von Pygame, das Festlegen der Fenstergröße, die Verwendung der Schriftart, die Definition der Menüoptionen und die Hauptschleife. In der Hauptschleife werden Ereignisse behandelt, die Auswahl im Menü geändert und die entsprechenden Aktionen ausgeführt.
Einstellungen:
Die Einstellungen des Spiels werden in einer separaten Datei mit dem Namen "settings.py" definiert. Die Einstellungen umfassen die Breite und Höhe des Fensters, die Bildwiederholrate (FPS) sowie verschiedene Einstellungen für den Spieler und den Feind.
Funktionsweise:
Das Spiel "TopDown" bietet ein Menü mit verschiedenen Optionen. Durch Drücken der Pfeiltasten nach oben und unten kann der Benutzer die Option auswählen, und durch Drücken der Eingabetaste kann die ausgewählte Option ausgeführt werden.
    • Wenn die Option "Start" ausgewählt wird, wird das Spiel initialisiert und die run()-Methode der Game-Klasse aufgerufen, um das Spiel zu starten.
    • Wenn die Option "Einstellungen" ausgewählt wird, werden die aktuellen Einstellungen angezeigt und der Benutzer kann sie ändern. Die geänderten Einstellungen werden in der Datei "settings.py" gespeichert.
    • Wenn die Option "Schließen" ausgewählt wird, wird das Spiel beendet.

Anpassung der Einstellungen:
Die Einstellungen können im Menü "Einstellungen" geändert werden. Der Benutzer kann eine Zahl von 0 bis 11 eingeben, um die gewünschte Einstellung auszuwählen. Nach der Auswahl wird der aktuelle Wert angezeigt und der Benutzer wird aufgefordert, den neuen Wert einzugeben. Die geänderten Werte werden in der Datei "settings.py" aktualisiert.
Hier ist ein Überblick über die verschiedenen Einstellungen:
Auflösung:
    • WIDHT: Die Breite des Fensters.
    • HEIGHT: Die Höhe des Fensters.
    • FPS: Die Bildwiederholrate (Frames pro Sekunde).

Spieler-Einstellungen:
    • PLAYER_SPEED: Die Geschwindigkeit des Spielers.
    • PLAYER_FUEL: Der Kraftstoff des Spielers.
    • PLAYER_FUEL_DEPLETION_RATE: Die Rate, mit der sich der Kraftstoff des Spielers verringert.
    • PLAYER_FUEL_REGEN_RATE: Die Rate, mit der sich der Kraftstoff des Spielers regeneriert.
    • PLAYER_CARGO: Die Ladung des Spielers.
Feind-Einstellungen:
    • ENEMEY_SPEED: Die Geschwindigkeit des Feindes.
    • ENEMEY_STOLE: Die Rate, mit der der Feind Ladung stiehlt.
    • ENEMEY_RANGE: Der Erfassungsbereich des Feindes.

Dateiänderungen:
Beim Ändern der Einstellungen wird die Datei "settings.py" gelesen und ihre Inhalte in einer Liste gespeichert. Die Liste wird entsprechend der ausgewählten Einstellung geändert. Anschließend wird eine neue Datei "nwsettings.py" erstellt und die geänderte Liste in diese Datei geschrieben. Die Berechtigungen der Originaldatei werden auf die neue Datei kopiert, und die Originaldatei wird umbenannt. Zuletzt wird die neue Datei umbenannt und erhält den Namen der Originaldatei.
Dieser Vorgang stellt sicher, dass die Originaldatei vor Änderungen gesichert wird und die aktualisierten Einstellungen in der Datei "settings.py" gespeichert werden.
Bitte beachte, dass die Dokumentation den Code erklärt, aber nicht alle möglichen Ausführungspfade oder Spezialfälle berücksichtigt.

Player.py:
Einleitung: Die Datei player.py enthält die Implementierung der Spielerklasse für das Pygame-Spiel. Diese Klasse repräsentiert den Spielercharakter und definiert seine Eigenschaften, Funktionen und Interaktionen in der Spielumgebung.
    1. Klassenstruktur: Die Klasse "Player" erbt von der Klasse "pygame.sprite.Sprite", um als Sprite-Objekt in der Spielumgebung verwendet zu werden. Sie enthält folgende Hauptkomponenten:
    • Konstruktor: Der Konstruktor initialisiert die verschiedenen Eigenschaften des Spielers, darunter Position, Grafiken, Treibstoff, Ladung, Geschwindigkeit und Kollisionsobjekte. Außerdem werden die Animationsframes für die Bewegung in verschiedenen Richtungen geladen.
    • Eingabe (input): Die Methode "input" verarbeitet die Tastatureingaben des Spielers und aktualisiert die Richtungsvektoren des Spielers entsprechend. Diese Methode ermöglicht es dem Spieler, den Charakter nach oben, unten, links und rechts zu bewegen.
    • Bewegung (move): Die Methode "move" berechnet die neue Position des Spielers basierend auf seiner aktuellen Geschwindigkeit und Richtung. Dabei werden Kollisionen mit anderen Spielobjekten berücksichtigt. Die Ausdauer des Spielers wird ebenfalls aktualisiert, und wenn die Ausdauer auf 0 sinkt, kann sich der Spieler nicht mehr bewegen.
    • Kollision (collision): Die Methode "collision" behandelt Kollisionen des Spielers mit anderen Spielobjekten. Je nach Art des kollidierenden Objekts werden entsprechende Aktionen ausgeführt. Zum Beispiel kann der Spieler Treibstoff oder Ladung aufnehmen oder eine Gewinnanimation abspielen, wenn bestimmte Bedingungen erfüllt sind.
    • Aktualisierung (update): Die Methode "update" wird regelmäßig aufgerufen, um den Spieler zu aktualisieren. Sie ruft die Eingabe- und Bewegungsmethoden auf und aktualisiert auch die Animation des Spielers basierend auf seiner aktuellen Richtung und Geschwindigkeit.
    3. Verwendung: Die Player-Klasse kann in einem Pygame-Spiel verwendet werden, um den Spielercharakter zu repräsentieren und seine Interaktionen mit der Spielumgebung zu steuern. Durch die Verwendung der definierten Methoden kann der Spieler den Charakter steuern, mit anderen Objekten kollidieren und verschiedene Aktionen ausführen.
       
KI-Klasse (AI):
Die Datei enemy.py enthält die Implementierung der KI-Klasse für das Pygame-Spiel. Diese Klasse repräsentiert einen KI-gesteuerten Gegner und definiert seine Eigenschaften, Funktionen und Interaktionen in der Spielumgebung.
    1. Klassenstruktur: Die Klasse "AI" erbt von der Klasse "pygame.sprite.Sprite", um als Sprite-Objekt in der Spielumgebung verwendet zu werden. Sie enthält folgende Hauptkomponenten:
    • Konstruktor: Der Konstruktor initialisiert die verschiedenen Eigenschaften der KI, einschließlich Position, Grafiken, Geschwindigkeit und Kollisionsobjekte.
    • Aktualisierung (update): Die Methode "update" wird regelmäßig aufgerufen, um die KI zu aktualisieren. Zunächst wird überprüft, ob die KI den Spieler berührt, und falls ja, wird die Ladung des Spielers entsprechend reduziert. Anschließend wird die Entfernung zum Spieler berechnet und basierend darauf entschieden, ob sich die KI auf den Spieler zubewegen soll oder nicht. Die Bewegung der KI wird mithilfe von Richtungsvektoren und der festgelegten Geschwindigkeit berechnet. Die Verwendung von Richtungsvektoren ermöglicht eine präzise und effiziente Berechnung der Bewegung der KI. Ein Richtungsvektor ist ein Vektor, der die Richtung und den Betrag der Bewegung angibt. In diesem Fall wird der Richtungsvektor von der KI zum Spieler berechnet, indem die Differenz der Positionen des Spielers und der KI gebildet wird. Dieser Vektor gibt die Richtung an, in die sich die KI bewegen sollte, um den Spieler zu erreichen. Um eine reibungslose Bewegung zu gewährleisten, wird der Richtungsvektor anschließend normalisiert, um sicherzustellen, dass er eine Länge von 1 hat. Dies ermöglicht eine konsistente Geschwindigkeit der KI, unabhängig von der Entfernung zum Spieler. Die Richtung wird beibehalten, während der Betrag des Vektors auf die festgelegte Geschwindigkeit der KI skaliert wird. Die berechneten Richtungsvektoren werden dann mit der Geschwindigkeit multipliziert, um den tatsächlichen Versatz der KI-Position zu erhalten. Durch Hinzufügen dieses Versatzes zur aktuellen Position der KI wird die neue Position berechnet und die KI entsprechend bewegt. Kollisionen mit anderen Spielobjekten werden ebenfalls berücksichtigt, um eine korrekte Bewegung sicherzustellen. Die KI überprüft, ob ihre Hitbox mit den Hitboxen anderer Objekte kollidiert. Bei einer Kollision werden die Positionen der KI angepasst, um Kollisionen zu vermeiden und die KI korrekt zu positionieren. Durch die Verwendung von Richtungsvektoren und einer effizienten Berechnung der Bewegung kann die KI reaktionsschnell und realistisch auf den Spieler reagieren und in der Spielumgebung navigieren. Dies trägt zur Schaffung einer ansprechenden und herausfordernden Spielerfahrung bei.

WhiteBox Test:

Überprüfe, ob die Ladung des Spielers korrekt reduziert wird, wenn die KI den Spieler berührt.
        ◦ Teste den Fall, in dem die KI den Spieler berührt und die Ladung des Spielers nicht leer ist.
        ◦ Teste den Fall, in dem die KI den Spieler berührt und die Ladung des Spielers bereits leer ist.
        ◦ Teste den Fall, in dem die KI den Spieler nicht berührt.
    2. Überprüfe, ob die Berechnung der Entfernung zum Spieler korrekt ist.
        ◦ Teste die Entfernung zwischen der KI und dem Spieler, wenn sie sich auf demselben Punkt befinden.
        ◦ Teste die Entfernung zwischen der KI und dem Spieler in verschiedenen Richtungen und Abständen.
        ◦ Teste die Entfernung, wenn der Spieler außerhalb des Bereichs der KI ist.
    3. Überprüfe, ob die KI sich korrekt auf den Spieler zubewegt.
        ◦ Teste die Bewegung der KI in Richtung des Spielers in verschiedenen Szenarien.
        ◦ Teste die Bewegung der KI, wenn der Spieler außerhalb des Bereichs der KI ist.
        ◦ Teste die Bewegung der KI, wenn der Spieler sich von der KI entfernt.
    4. Überprüfe, ob die Kollisionserkennung mit anderen Objekten korrekt funktioniert.
        ◦ Teste die Kollision der KI mit verschiedenen Hindernissen und überprüfe, ob die Bewegung korrigiert wird.
        ◦ Teste die Kollision der KI mit dem Spieler und überprüfe, ob die Position korrigiert wird.
        ◦ Teste die Kollision der KI mit anderen KIs und überprüfe, ob die Positionen beider KIs korrigiert werden.
    5. Überprüfe, ob die KI-Position korrekt aktualisiert wird.
        ◦ Teste die neue Position der KI nach der Bewegung und überprüfe, ob sie der erwarteten Position entspricht.
        ◦ Teste die Aktualisierung der KI-Position in verschiedenen Szenarien, einschließlich der Berücksichtigung von Kollisionen.
    6. Überprüfe die Performance der Aktualisierungsmethode.
        ◦ Teste die Aktualisierungsgeschwindigkeit der KI in Bezug auf die Anzahl der anderen Objekte auf dem Spielfeld.
        ◦ Teste die Aktualisierungsgeschwindigkeit der KI bei verschiedenen Geschwindigkeitseinstellungen.





Benutzer Doku:
Benutzerdokumentation: Spielanleitung
Willkommen zur Benutzerdokumentation des Python-Spiels zur Simulation von Warentransporten! In diesem Spiel übernimmst du die Rolle eines LKW-Fahrers und hast die Aufgabe, Güter von einem Startpunkt zu einem Endpunkt zu transportieren. Dabei musst du verschiedene Herausforderungen bewältigen und deine Ressourcen effizient nutzen. Folgende Anleitung hilft dir, das Spiel zu spielen und auf wichtige Aspekte zu achten:
    1. Installation:
        ◦ Stelle sicher, dass du Python auf deinem Computer installiert hast.
        ◦ Lade die erforderlichen Spieldateien herunter und entpacke sie in einen Ordner deiner Wahl.
    2. Spielstart:
        ◦ Öffne die Kommandozeile oder ein Terminal und navigiere zum Verzeichnis, in dem du die Spieldateien gespeichert hast.
        ◦ Starte das Spiel, indem du den Befehl "python game.py" eingibst.
    3. Spielziel:
        ◦ Dein Ziel ist es, die Gütermenge sicher vom Startpunkt zum Endpunkt zu transportieren.
        ◦ Achte darauf, dass der Hubschrauber nicht mehr als 20% der Waren entwendet und dass dein LKW ausreichend Treibstoff hat, um die Aufgabe zu erfüllen.
    4. Steuerung:
        ◦ Verwende die Pfeiltasten (oben, unten, links, rechts) zur Steuerung deines LKWs.
        ◦ Drücke die Leertaste, um den LKW zu betanken, wenn du eine Tankstelle erreichst.
    5. Spielablauf:
        ◦ Bewege deinen LKW entlang der Straße zum Endpunkt, während du Güter transportierst.
        ◦ Achte auf den Hubschrauber, der versucht, Waren zu stehlen. Vermeide Kollisionen mit dem Hubschrauber.
        ◦ Suche nach Tankstellen, um den Treibstoff deines LKWs aufzufüllen.
        ◦ Behalte die Treibstoffanzeige im Auge und tanke rechtzeitig nach, um nicht liegenzubleiben.
    6. Szenarien und Regeln:
        ◦ Das Spiel beinhaltet verschiedene Szenarien, um den Realismus zu steigern.
        ◦ Die Wahrscheinlichkeit, dass der Hubschrauber Waren stiehlt, erhöht sich mit der Zeit.
        ◦ Die Entfernung zwischen Start- und Endpunkt kann variieren, ebenso wie die Anzahl der Tankstellen auf dem Weg.
        ◦ Du kannst das Spiel jederzeit neu starten, um neue Szenarien zu erleben.
    7. Spielende:
        ◦ Das Spiel endet, wenn du den Endpunkt erreicht hast und dabei die Vorgaben erfüllt hast.
        ◦ Du gewinnst, wenn der Hubschrauber nicht mehr als 20% der Waren entwendet und dein LKW ausreichend Treibstoff hat.
        ◦ Du verlierst, wenn der Hubschrauber mehr als 20% der Waren stiehlt oder dein LKW keinen Treibstoff mehr hat.
    8. Benutzer- und Programmdokumentation:
        ◦ Neben dieser Spielanleitung gibt es auch eine detaillierte Benutzer- und Programmdokumentation.
        ◦ Die Benutzerdokumentation erklärt die Installation des Spiels und die Interaktion mit dem Spiel
