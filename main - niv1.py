from random import *

class Place():

    def __init__(self,numero,mobiliteReduite=False):
        self.mobiliteReduite = mobiliteReduite
        self.emplacement = numero
        self.disponible = True 
        self.plaqueImmat = ""
    
    def set_indisponibilite(self,plaqueImmat):
        self.plaqueImmat = plaqueImmat
        self.set_disponibilite(False)

    def set_disponibilite(self,disponibilite):
        self.disponible = disponibilite
    
    def get_disponibilite(self):
        if self.disponible:
            return "disponible"
        else:
            return f"non disponible (occupé par le véhicule '{self.plaqueImmat}')"

class Parking():

    def __init__(self,nom="",nbPlace=27):
        self.places = []
        self.nbPlace = nbPlace
        self.init_places(self.nbPlace)
        self.nom = nom

    def get_nbPlace(self):
        return self.nbPlace

    def get_place(self, emplacement):
        if emplacement < len(self.places):
            return [self.places[emplacement].emplacement, self.places[emplacement].get_disponibilite(), self.places[emplacement].mobiliteReduite ]
        else:
            return "cet emplacement n'existe pas"

    def init_places(self,nbPlace):
        for num in range(0,self.nbPlace):
            self.places.append(Place(num,randint(0,1)))

parking=Parking("Boboda parking",27)
print(f"Parking '{parking.nom}', Bienvenue au niveau -1 : que voulez vous faire ?")

print(f"L'emplacement n°3 est {parking.places[2].get_disponibilite()}")

parking.places[0].set_indisponibilite("123-AA-456")
print(f"L'emplacement n°0 est {parking.places[0].get_disponibilite()}")

for num in range(0, parking.nbPlace):
    print(f"L'emplacement n°{num} est {parking.places[num].get_disponibilite()}")

