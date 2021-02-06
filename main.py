from Wikigame import *
from utils import *
jeuTermine = False

# print("Bienvenue dans le jeu de Wikipédia ! ")
# print("Le principe est simple, une page de départ et d'arrivée vont être tirée au sort")
# print("A vous d'y arriver le plus vite possible")
# print("Bonne chance !")

fenetre = Tk()

game = Wikigame(fenetre)
fenetre.mainloop()

#TODO Mettre un message au début et à la fin du jeu
#TODO Faire en sorte que les accents fonctionnent à l'afficage urllib quote et unquote (avec un parse avant et apres)
#TODO Faire en sorte que ça ne soit pas les liens qui s'affichent mais
#les résumés
#TODO Ajouter une erreur si jamais la page est vide et revenir à la page précédente


