# Arbeitsauftrag: Übernehmt den Messdaten-Checker

3BHITS · Softwareentwicklung · Zweierteams · Richtwert: 4–6 Unterrichtseinheiten

## Ausgangslage

Ihr übernehmt ein kleines, fehlerhaftes Python-Projekt ohne Klassen.
Es verwendet Funktionen, Listen, Schleifen und Textdateien. Es enthält fünf
gezielt eingebaute Fehler. Findet ihre Ursachen und behebt sie nachvollziehbar.

## Verbindliches Sollverhalten

Eine Datei enthält pro nicht leerer Zeile eine gültige Temperaturzahl mit
Dezimalpunkt. Leere Zeilen werden ignoriert. Das Programm zeigt Anzahl,
Mittelwert (Summe geteilt durch Anzahl), Maximum und die Anzahl der Werte
**streng größer als 25 °C**. Mittelwert und Maximum erscheinen mit zwei
Nachkommastellen. Negative Temperaturen müssen funktionieren.
Bei einer leeren Datei erscheint `Keine Messwerte vorhanden.`; es wird keine
Statistik berechnet. Unbekannte Dateinamen und ungültiger Text gehören erst zur
Zusatzaufgabe. Wählt zunächst ausschließlich die mitgelieferten Dateien.

## Einstieg

Python 3.10 oder neuer; keine zusätzlichen Pakete. Im Projektordner:

```sh
python messdaten.py
```

Unter Windows alternativ `py messdaten.py`, auf manchen Systemen `python3`.
Gebt danach beispielsweise `normal.txt` ein. Dateien werden relativ zum Skript
gefunden. Einlesen mit `open`, Umwandlung mit `float`, Listen mit `append` und
Formatierung mit `:.2f` dürft ihr vorab gemeinsam besprechen.

## Prüffälle

| Datei | Anzahl | Mittelwert | Maximum | Über 25 °C |
|---|---:|---:|---:|---:|
| normal.txt | 4 | 25.00 | 30.00 | 1 |
| frost.txt | 3 | -5.00 | -2.00 | 0 |
| einzelwert.txt | 1 | 25.00 | 25.00 | 0 |
| mit_leerzeilen.txt | 3 | 20.00 | 30.00 | 1 |
| leer.txt | – | Keine Messwerte vorhanden. | – | – |

Ergänzt mindestens einen eigenen Prüffall. Ein Prüffall kann mehrere Fehler
zeigen. Verschiedene Symptome können dieselbe Ursache haben; erstellt keine
mehrfachen Issues für denselben Fehler.

## Euer Workflow

1. Repository klonen, starten und alle Prüffälle ausprobieren.
2. Fehler als Issues dokumentieren: Schritte, Erwartung, tatsächliches Ergebnis.
   Nutzt die Vorlage unter GitHub → Issues → New issue.
3. Vor jeder Korrektur aktuellen `main` holen und einen Branch erstellen.
4. Mit Breakpoint, Einzelschritten und Variablenansicht die Ursache untersuchen.
   Notiert im Pull Request eine konkrete Beobachtung des Debuggers.
5. Nur den gewählten Fehler beheben, gezielt committen und Branch pushen.
6. Pull Request nach `main` öffnen, Issue mit `Closes #NUMMER` verknüpfen.
7. Partner:in prüft Änderung und führt den beschriebenen Prüffall selbst aus.
8. Nach erfolgreicher Prüfung mergen, lokalen `main` aktualisieren, Branch löschen.
9. In einem eigenen Dokumentations-Branch die README vervollständigen und per
   Pull Request übernehmen. Den Arbeitsauftrag nicht als README kopieren.

Arbeitet zu Beginn nacheinander: eine Person korrigiert, die andere prüft;
wechselt die Rollen. Jede Person erstellt mindestens einen Fix und prüft einen
fremden Pull Request. Änderungen direkt auf `main` sind nicht vorgesehen.

### Befehle als Hilfe

Platzhalter wie NUMMER und BRANCHNAME durch eure tatsächlichen Werte ersetzen.
Vor einem Wechsel sollen eigene Änderungen committed oder anderweitig gesichert sein.

```sh
git switch main
git pull --ff-only
git switch -c fix/NUMMER-kurzer-name
# Fehler untersuchen, ändern und prüfen
git add messdaten.py
git commit -m "Fix: Mittelwert korrekt berechnen"
git push -u origin fix/NUMMER-kurzer-name
```

Pull Request, Review und Merge erfolgen auf GitHub. Danach:

```sh
git switch main
git pull --ff-only
git branch -d BRANCHNAME
```

Verwendet in dieser Übung auf GitHub **Create a merge commit**, damit der lokale
Branch anschließend mit `-d` gelöscht werden kann. Den Remote-Branch über
`Delete branch` im gemergten Pull Request entfernen. Ein Push allein führt die
Änderung noch nicht in `main` zusammen.

## README-Checkliste

- Projektname und Zweck
- Voraussetzungen (Python-Version, zusätzliche Pakete)
- Installation bzw. Klonen und Start mit konkreten Befehlen
- Beispiel: Dateiname und erwartete Ausgabe
- Datenformat und Umgang mit leeren Dateien
- Tatsächliche Einschränkungen und ggf. offene Issues

## Abgabe und Erfolgskriterien

Abgabe: Repository-Link. Alle fünf Fehler sind behoben, die mitgelieferten und
eigenen Prüffälle stimmen. Issues und Pull Requests dokumentieren Ursache,
Änderung und Prüfung. Mindestens ein Debugger-Befund pro Fix, Reviews durch die
andere Person, verständliche Commits und eine brauchbare README sind sichtbar.
Keine Lösung als Ganzes ersetzen: Jede Korrektur soll einzeln nachvollziehbar sein.

## Zusatz: bewusster Merge-Konflikt

Erst nach der Pflichtaufgabe: Beide erstellen vom selben aktuellen `main` je
einen Branch und ändern dieselbe Zeile der README unterschiedlich. Ersten PR
mergen. Im zweiten Branch `git fetch origin` und `git merge origin/main` ausführen.
Konfliktmarker bearbeiten, eine sinnvolle gemeinsame Fassung herstellen,
`git add README.md`, committen und pushen. Anschließend zweiten PR prüfen/mergen.

## Zusatz: robuste Eingabe

Fehlende Datei und nichtnumerische Zeilen mit verständlichen Meldungen behandeln.
Legt vorher fest, ob das Programm bei ungültigen Zahlen abbricht oder sie überspringt.
