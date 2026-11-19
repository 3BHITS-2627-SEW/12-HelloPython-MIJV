
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
    print(*meineListe, sep=" - ")
    # * entpackt die liste
    #und fuegt diese 1:1 als parameter in den funktionsaufruf ein
    print("das vierte element ist: ", meineListe[3], sep="\n")

    #die liste umdrehen
    # meineListe.reverse()
    # print("die Liste verkehrt:", meineListe )

    #veraendere nicht die original-Liste 
    verkehrteListe = meineListe.copy()
    #jetzt kann die kopie gedreht werden
    verkehrteListe.reverse()
    print("die kopierte verkehrte liste: ", verkehrteListe)

    #ersetze elemente: 
    meineListe[3] = "vier"
    print(meineListe)

    #wie viele elemente hat die liste?
    print(f"In der liste sind {len(meineListe)} Elemente!")
    print(f"In der verkehrten liste {verkehrteListe.__len__()}")

    #verwende Pop
    print(f"wir nehmen das element {verkehrteListe.pop} heraus")
    print(" liste: ", meineListe)

    for einListenEintrag in meineListe:
          print("Ein Eintrag in der liste", einListenEintrag, sep=": ")

    for i in range(11): 
          print(f"{i}, ")

    for i in range(1, 10+1, 2):
          print(f"{i}, ")
          

if __name__ == "__main__":
        #umgang mit den default-parametern
        # demo vorgezeigt zur befuellung
        # auf verschiedene arten 
        # main() #verwenden den default parameter
        # main("schon etwas")
        main(einZweiterParameter="November", einParameter="is no None")