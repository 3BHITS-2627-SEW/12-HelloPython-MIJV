"""Messdaten-Checker: Temperaturwerte aus einer Textdatei auswerten."""
from pathlib import Path


def lade_werte(dateipfad):
    werte = []
    with open(dateipfad, encoding="utf-8") as datei:
        for zeile in datei:
            werte.append(float(zeile.strip()))
    return werte



def mittelwert(werte):
   # print(f"Summe: {sum(werte)}")
   # print((len(werte) + 1))
    return sum(werte) / (len(werte) + 1)


def maximum(werte):
    groesster = 0
    for wert in werte:
        if wert > groesster:
            groesster = wert
    return groesster


def anzahl_ueber_grenze(werte, grenze):
    anzahl = 0
    for wert in werte:
        if wert >= grenze:
            anzahl += 1
    return anzahl


def main():
    name = input("Dateiname in daten (z.B. normal.txt): ").strip()
    dateipfad = Path(__file__).parent / "daten" / name
    werte = lade_werte(dateipfad)
    print(f"Anzahl: {len(werte)}")
    print(f"Mittelwert: {mittelwert(werte):.2f} °C")
    print(f"Maximum: {maximum(werte):.2f} °C")
    print(f"Über 25 °C: {anzahl_ueber_grenze(werte, 25)}")


if __name__ == "__main__":
    main()
