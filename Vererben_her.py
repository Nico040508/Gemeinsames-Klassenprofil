class Einwohner:
    def __init__(self, einkommen):
        self.einkommen = int(einkommen)
        
    def zuVersteuerndesEinkommen(self):
        steuer = 0.1
        if self.einkommen >= 10:
            steuer_abgabe = int(self.einkommen * steuer)
        else:
            steuer_abgabe = 1
        return steuer_abgabe

class Bauer(Einwohner):
    pass
        
class Leibeigener(Bauer):
        
    def zuVersteuerndesEinkommen(self):
        steuer = 0.1
        if self.einkommen <= 12:
            steuer_abgabe = 0
        elif self.einkommen <= 22:
            steuer_abgabe = 1
        else:
            steuer_abgabe = int((self.einkommen - 12) * steuer)
        return steuer_abgabe
        
class König(Einwohner):
    
    def zuVersteuerndesEinkommen(self):
        steuer = 0
        steuer_abgabe = int(self.einkommen * steuer)
        return steuer_abgabe
    
class Adel(Einwohner):
         
    def zuVersteuerndesEinkommen(self):
        steuer = 0.1
        if self.einkommen >= 200:
            steuer_abgabe = int(self.einkommen * steuer)
        else:
            steuer_abgabe = 20
        return steuer_abgabe
        
class Klerus(Einwohner):
    
    def zuVersteuerndesEinkommen(self):
        steuer = 0.1
        if self.einkommen <= 5:
            steuer_abgabe = 0
        elif self.einkommen <= 15:
            steuer_abgabe = 1
        else:
            steuer_abgabe = int((self.einkommen - 5) * steuer)
        return steuer_abgabe
       
def gesamtsteuer(liste):
    gesamtsteuer_g = 0
    for element in liste:
        steuer_abgabe_element = element.zuVersteuerndesEinkommen() #--> Hier war der Fehler () haben gefehlt, damit wurde die Methode nicht aufgerufen
        gesamtsteuer_g = gesamtsteuer_g + steuer_abgabe_element
    print("Die Gesamtsteuer ist: ", gesamtsteuer_g)
    return(gesamtsteuer_g)
   
    
    
        
bauer1 = Bauer("9")
print(bauer1.zuVersteuerndesEinkommen())

sklave1 = Leibeigener("48")
print(sklave1.zuVersteuerndesEinkommen())

könig = König("67676767")
print(könig.zuVersteuerndesEinkommen())

adel1 = Adel("190")
print(adel1.zuVersteuerndesEinkommen())

klerus1 = Klerus("25")
print(klerus1.zuVersteuerndesEinkommen())

liste_einwohner = [bauer1, sklave1, könig, adel1, klerus1]
gesamtsteuer(liste_einwohner)
