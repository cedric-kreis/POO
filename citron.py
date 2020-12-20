# -*- coding: utf-8 -#-
#-------------------------------------------------------------------------------
#
# Auteur        : Cédric Kreis
# Type          : Script employanr une classe
# Programme     : Instanciation d'un citron
# Fonctions     : Ce script choisit aléatoirement dans des listes un nom,
#                 un poids et une couleur pour une instance d'un citron.
# Création      : 19.12.2020
# Modifié le    : -
# Version       : 1
#
# OS            : MacOSX
# Python        : 2.7.10
#
#
#-------------------------------------------------------------------------------

#Librairie permettant l'éxecution de choix aléatoire
import random

class Citron:

    # Constructeur -> valeurs par défaut
    def __init__(self, couleur, nom, poids, unite):
        self.couleur = couleur
        self.nom = nom
        self.poids = poids
        self.unite = unite


# Utilisation d'une liste pour choisir un poids aléatoirement
pliste = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(1):
    poidsalea = random.choice(pliste)

# Utilisation d'une liste pour choisir un nom aléatoirement
nliste = ['Meyer', 'Lime', 'Caviar', 'Yuzu']
for i in range(1):
    nomalea = random.choice(nliste)

# Utilisation d'une liste pour choisir une couleur aléatoirement
cliste = ['vert','jaune']
for i in range(1):
    couleuralea = random.choice(cliste)


#Affectation aux variables des données proveneant du code en aléatoire
couleur = couleuralea
nom = nomalea
poids = poidsalea

#Contrôle du poids afin d'adapter l'orthographe
if poids > 1:
    unite = "grammes"
else :
    unite = "gramme"


#Instanciation de la class Citron
modele = Citron(couleur, nom, poids, unite)


#Affichage du travail
print ""
print "Couleur :", modele.couleur
print "Nom     :", modele.nom
print "Poids   :", modele.poids, modele.unite
print ""
