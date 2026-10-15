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