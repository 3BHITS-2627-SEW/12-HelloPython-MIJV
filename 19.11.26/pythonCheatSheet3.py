
#nicht zuleassig non-default parameter nach default parameter
#korrekte schreibweise - folge umdrehen
def main(einParameter : str = "nix", einZweiterParameter : str = "aNix") -> None:
    print("ein Python Cheatsheet!")

    meineListe : list = ["eins", "zwei", "drei", "viele..."]

    #ausgabe
    print("Mein Parameter einParameter: ", einParameter)
    print(f"Mein Parameter einZweiterParameter: \
          {einZweiterParameter}")

    #werte an liste
    meineListe.append("noch viel mehr ..")
    #die liste anzeigen
    print(meineListe)
    #anzeife geht ganz einfach, warum???
    #testen mit meineklasse ob das auch so einfach geht

    # 0. importiere die bibliothek
    # schlechte idee: an dieser stelle importieren
    from mein_paket.meineKlasse import MeineKlasse

    # 1. ein neues objekt anlegen
    einObjekt = MeineKlasse()

    # 2. mit print ausgeben
    print(einObjekt)

if __name__ == "__main__":
        #umgang mit den default-parametern
        # demo vorgezeigt zur befuellung
        # auf verschiedene arten 
        # main() #verwenden den default parameter
        # main("schon etwas")
        main(einZweiterParameter="November", einParameter="is no None")