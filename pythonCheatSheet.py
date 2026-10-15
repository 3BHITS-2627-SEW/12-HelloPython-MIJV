#variable
eineVariable = 13
print("eineVariable", eineVariable)
eineVariable = "blbslblsbls"
print("eineVariable", eineVariable)

#Typisierung in Python: Ducktyping

eineZweiteVariable : int = 14
print("einezweitevariable", eineZweiteVariable**3)
eineZweiteVariable = "Text"

#erzeugt leider erste den fehler zur laufzeit
#print("einezweitevariablr", einezweitevariable**3)

datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)
eineVariable = 15

datenTyp = type(eineVariable)
print("datentyp von eineVariable: ", datenTyp)

#formatierte Ausgabe
#C: printf("Zahl lautet %i \nund ist cool!", eineVariable)
print("Zahl lautet %i\n und ist cool!", eineVariable)
#formatierte Strings
einText = f"Zahl lautet {eineVariable**2} \n und ist cool!"
print("Zahl lautet ", (eineVariable**2)," \n und ist cool!")
#Typ-Umwandeln
#(type-Conversion)
einString = str((eineVariable**2)) #wandle zahl in text um
alternativtext = "Zahl lautet "+einString+"\n und ist cool!"
print(einText)
print("alternativtext:" ,alternativtext)

#eingabe von der Kommandozeile:
#int i = 0
#printf("bitte zahl eingeben:\n ");
#scanf(%i);
eingelesenezahl = input("Bitte zahl eingeben: ")
print("Zahl eingelesen vom Typ", type(eingelesenezahl))