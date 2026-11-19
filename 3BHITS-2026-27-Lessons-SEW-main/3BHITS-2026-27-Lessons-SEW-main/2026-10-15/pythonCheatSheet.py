## Datei: pythonCheatSheet.py
## Ausfuehren: python pythonCheatSheet.py
## BZW: py pythonCheatSheet.py

## Dies ist ein kleines Cheat-Sheet fuer die
## Verwendung von Python fuer C und C++ Programmierer

# Variable
#int eineZahl = 43;
eineVariable = 13 
print("eineVariable:",eineVariable)
eineVariable = "blablabla"
print("eineVariable:",eineVariable)
# Typisierung in Python: Ducktyping 
# Daher: bitte immer nach Moeglichkeit typisieren:
eineZweiteVariable : int = 14
print("eineZweiteVariable", eineZweiteVariable**3 )
eineZweiteVariable = "Text"
# erzeugt leider erste den Fehler zur Laufzeit!
#print("eineZweiteVariable", eineZweiteVariable**3 )

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)
eineVariable = 15

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)

# formatierte Ausgabe
# C: printf("Zahl lautet %i \n und ist Cool!", eineVariable);
print("Zahl lautet %i \n und ist Cool!", eineVariable)
#formatierte Strings
einText = f"Zahl lautet {eineVariable**2} \n und ist Cool!"
print("Zahl lautet ",(eineVariable**2)," \n und ist Cool!")
# Typ-Umwandeln
# (Type-Conversion)
einString = str((eineVariable**2))# Wandle Zahl in Text um
alternativText = "Zahl lautet "+einString+" \n und ist Cool!"
print(einText)
print("Alternativ-Text:",alternativText)

# Eingabe von der Kommandozeile:
# int i=0;
# printf("Bitte Zahl eingeben:\n");
# scanf(&i);
eingeleseneZahl = int(input("Bitte Zahl eingeben: "))
print("Zahl eingelesen vom Typ",type(eingeleseneZahl))

# Funktionen
# int main(void) {
#     printf("Hallo Funktion!");
# }
def main():
    print("Hallo Main!")


main()