from random import *
from array import *
import re

class Place():

    def __init__(self,niveau,numero,mobiliteReduite=False):
        self.mobiliteReduite = mobiliteReduite
        self.emplacement = numero
        self.niveau = niveau
        self.disponible = True 
        self.plaqueImmat = ""
        self.code = ""
    
    def set_indisponibilite(self,plaqueImmat):
        self.plaqueImmat = plaqueImmat
        self.set_disponibilite(False)
    
    def set_liberer(self):
        self.plaqueImmat = ""
        self.set_disponibilite(True)    

    def set_disponibilite(self,disponibilite):
        self.disponible = disponibilite
    
    def get_disponibilite(self):
        if self.disponible:
            return True
        else:
            return False

    def get_disponibiliteTxt(self):
        if self.disponible:
            return "disponible"
        else:
            return f"occupé (véhicule '{self.plaqueImmat}'/'{self.code}')"


class Parking():

    def __init__(self,nom="",nbNiveau=1,nbPlace=27):
        self.places = []
        self.nbPlace = nbPlace
        self.nbNiveau = nbNiveau
        self.init_places()
        self.nom = nom
        print(f"Bienvenu dans notre parking '{nom}'. Il contient {nbNiveau*nbPlace} places réparties sur {nbNiveau} niveaux")

    def get_nbPlace(self):
        return self.nbPlace

    def get_place(self, niveau, emplacement):
        if emplacement < len(self.places):
            return [self.places[emplacement].emplacement, self.places[emplacement].get_disponibilite(), self.places[emplacement].mobiliteReduite ]
        else:
            return "cet emplacement n'existe pas"

    def init_places(self):
        for niv in range(0,self.nbNiveau):
            placesByNiveau = []
            for num in range(0,self.nbPlace):
                placesByNiveau.append(Place(niv,num,randint(0,1)))
            self.places.insert(niv,placesByNiveau)

    def afficher_parking(self, numNiveau = None):
        print(numNiveau)
        if not numNiveau:
            for niv in range(0,self.nbNiveau):
                for num in range(0, self.nbPlace):
                    print(f"L'emplacement n°{num} du niveau -{niv} est {self.places[niv][num].get_disponibiliteTxt()}") 
        else:
            for num in range(0, self.nbPlace):
                print(f"L'emplacement n°{num} du niveau -{numNiveau} est {self.places[numNiveau][num].get_disponibiliteTxt()}") 

parking=Parking("Boboda parking",1,2)
# parking.afficher_parking(1)
while True:
    action=int(input("Que voulez vous faire (1 - vous garez , 2 - récuperer votre véhicule) ? "))
    if action==3: # voir le parking
        parking.afficher_parking()
    if action==2: # récuperer la voiture
        plaqueImmat=input("Quelle est votre plaque d'immatriculation ? ")
        fin = False
        niveau = 0
        place = 0
        while not fin:
            print(place,niveau)
            if not parking.places[niveau][place].get_disponibilite():
                if parking.places[niveau][place].plaqueImmat == plaqueImmat:
                    print(f"Votre véhicule est stationné à l'emplacement N°{parking.places[niveau][place].emplacement} du niveau -{parking.places[niveau][place].niveau}")
                    parking.places[niveau][place].set_liberer()
                    place = 0
                    fin = True

            place += 1
            if place == parking.nbPlace:
                niveau += 1
                place = 0
            if niveau == parking.nbNiveau:
                print("Désolé votre véhicule n'est pas ici !")
                fin = True
    if action==1: # garer la voiture
        plaqueImmat=input("Quelle est votre plaque d'immatriculation ? ")
        code_valid = False
        while not code_valid:
            code=str(input("Votre code de recupération (format AAAA-123-AA)? "))
            code_valid = re.findall("[A-Z][A-Z][A-Z][A-Z]-[0-9][0-9][0-9]-[A-Z][A-Z]", code)
        dispo = False
        niveau = 0
        place = 0
        while not dispo:
            if parking.places[niveau][place].get_disponibilite():
                dispo = True
                parking.places[niveau][place].set_indisponibilite(plaqueImmat)
                print(f"la place n°{parking.places[niveau][place].emplacement} du niveau -{niveau} est disponible")
                parking.places[niveau][place].code = code
            else:
                place += 1
                if place == parking.nbPlace:
                    niveau += 1
                    place = 0
                if niveau == parking.nbNiveau:
                    print("Désolé le parking est plein")
                    dispo = True
        

