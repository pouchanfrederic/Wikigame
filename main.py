from Wikigame import *
from utils import *

#Message affiché dans la console
print("Bienvenue dans le jeu de Wikipédia ! ")
print("Le principe est simple, une page de départ et d'arrivée vont être tirée au sort")
print("A vous d'y arriver le plus vite possible")
print("Bonne chance !")

fenetre = Tk() #Génération de la fenêtre qui contient le jeu 

game = Wikigame(fenetre) #Permet de lancer le jeu en faisant appel au constructeur de la classe Wikigame
fenetre.mainloop() #Boucle qui permet de maintenir l'application ouverte


