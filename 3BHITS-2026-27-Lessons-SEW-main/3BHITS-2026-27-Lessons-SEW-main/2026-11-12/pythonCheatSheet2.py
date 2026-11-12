# Fortsetzung des Cheat-Sheets

# importieren von bibliotheken
import numpy

# benenne ein Paket um:
import numpy as npy

# nur eine Klasse aus einem Paket importieren
# und zusaetzlich umbenennen
from numpy import number as npynb

# alles importieren
from numpy import *

# eigene Bibliotheken bzw. Pakete importieren

# mit falscher __init__,py
#from mein_paket.meineKlasse import *
from mein_paket import *

def main():
    number1 = numpy.sqrt(4)
    print("Wurzel aus 4:", number1)
    number2 = npy.sqrt(16)
    print("Wurzel aus 16:", number2)
    # verwende number von npy
    #npy.number
    # verwende die Klasse Number, importiert via *
    #number.

    # Verwende die eigene Klasse:
    #MeineKlasse
    meinObjekt = MeineKlasse()
    print("Name vom Objekt:","PRIVATE")  #meinObjekt.__name)

    print("Welcher Monat ist aktuell?", meinObjekt.noNoneNovember())

    print("Der Name vom Objekt via getter: ", meinObjekt.get_name())

    meinObjekt.set_name("MeinObjekt")
    print("Namen nach andearung: ", meinObjekt.get_name())
    pass


if __name__ == "__main__":
    main()