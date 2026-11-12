# Erstelle eine Klasse in Python
class MeineKlasse:
    # Konstruktor
    def __init__(self):
        # self in Python enspricht dem this-pointer in C++

        # self.name wird eine Instanz-Variable
        self.__name = "EineKlasse"
        #pass # macht einfach gar nichts

        #eine methode
    def noNoneNovember(self):
        return("November!")

    #getter
    def get_name(self) -> str:
        return self.__name

    #setter
    def set_name(self, neuer_name : str) -> None:
        self.__name = neuer_name
        #pass