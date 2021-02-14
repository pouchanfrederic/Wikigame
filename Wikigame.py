from tkinter import *
from utils import *

clear = lambda: os.system('cls')


class Wikigame:

    def __init__(self, fenetre):
        #Constructeur de la classe wikigame 

        self.pageDeDepart = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard' #Lien au hasard, stocké dans la variable pageDeDepart
        self.pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard' #Lien au hasard, stocké dans la variable pageDArrivee

        self.fenetre = fenetre #Création de la fenêtre qui va contenir le jeu 
        self.fenetre.geometry("600x600") #Taille de la fenêtre
        self.fenetre.title("Wikigame par Frédéric Pouchan") #Titre de la fenêtre

        self.pageDeDepart, self.pageDArrivee = initializeVariables(self.pageDeDepart, self.pageDArrivee) #Appel de la méthode initializeVariable, en lui passant 2 paramètres
        self.url = self.pageDeDepart #car au début, la page en cours est la même que la page de départ
        self.compteur = 0 #Compteur qui permet de connaître le nombre de coup du joueur

        self.labelCompteur = Label(self.fenetre, text=("Compteur de coups : " + str(self.compteur))) #Label qui permet l'affichage du score du joueur
        self.labelCompteur.pack() #Ajout du label dans la fenêtre

        self.labelUrl = Label(self.fenetre, text=("Page en cours : " + urllib.parse.unquote(self.url.removeprefix("https://fr.wikipedia.org/wiki/")))) 
        #Label qui contient le nom de la page en cours, en ajout les accents pour améliorer la lisibilité
        self.labelUrl.pack() #Ajout du label dans la fenêtre de jeu 

        self.label = Label(self.fenetre, text=("Objectif : " + urllib.parse.unquote(self.pageDArrivee.removeprefix("https://fr.wikipedia.org/wiki/"))))
         #Label qui contient le nom de la page à atteindre, en ajout les accents pour améliorer la lisibilité
        self.label.pack()#Ajout du label dans la fenêtre de jeu 

        self.scrollbar = Scrollbar(self.fenetre, orient="vertical")
        #Barre de défilement pour améliorer la jouabilité dans la fenêtre de jeu 
        self.listbox = Listbox(self.fenetre, width=100, height=40, yscrollcommand=self.scrollbar.set)
        #Ajout de la barre de défilement à la liste de liens, pour qu'elles soient liées 

        self.scrollbar.config(command=self.listbox.yview)
        #Configuration de la barre de défilement
        self.scrollbar.pack(side="right", fill="y")

        self.submit = Button(self.fenetre, text='Valider', command=self.updateWindow)
        #Ajout du bouton qui permet de valider la selection
        self.submit.pack() #Ajout du bouton à la fenêtre de jeu 

        self.listbox.pack() #Ajout de la listbox à la fenêtre de jeu 

        self.selection = '' #Selection est la variable qui contient le lien contenu dans la selection de l'utilisateur à la souris

        self.url = self.pageDeDepart

        self.initializeWindow() #Appel de la méthode qui génère pageDeDepart et pageDArrivee
        

    def initializeWindow(self): #Méthode qui génère et remplit la fenêtre de jeu 
        listeDeLiens = getLinksFromUrl(self.url)  # Tous les liens de page liée à l'url donnée en paramètre
        compteurBoucle = 0
        if len(listeDeLiens) == 0: #Dans le cas où la page générée aléatoirement ne contienne pas de liens
            self.pageDeDepart = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
            self.url = self.pageDeDepart
            listeDeLiens = getLinksFromUrl(self.url)
            self.labelUrl['text'] = "Page en cours : " + getUrlDeSecours() #Actualiasation de l'affichage de la page en cours dans l'ihm

        for lien in listeDeLiens:
            compteurBoucle += 1
            lien = lien.removeprefix("/wiki/")
            self.listbox.insert(compteurBoucle, lien)

    def updateWindow(self): #Méthode qui permet d'update la fenêtre à chaque fois que l'utilisateur à choisit la page sur laquelle se rendre

        selectionVide = self.listbox.curselection()
        if len(selectionVide) == 0: #Ne rien faire si l'utilisateur n'a cliqué sur aucun lien
            return
        self.selection = self.listbox.get(self.listbox.curselection()) #Permet de récupèrer le lien de la selection
        listeDeLiens = getLinksFromUrl(("https://fr.wikipedia.org/wiki/"+ urllib.parse.quote(self.selection))) #Remplir la variable via la méthode getLinksFromUrl
        if len(listeDeLiens) == 0: #Ne rien faire si la liste de liens est vide
            return
        if ("https://fr.wikipedia.org/wiki/" + self.selection) != self.pageDArrivee: #Condition de victoire
            self.compteur += 1 #Incrémentation du compteur 
            self.labelCompteur['text'] = "Compteur de coups : " + str(self.compteur) #Actualisation de l'affiage du compteur dans l'ihm
            self.labelUrl['text'] = "Page en cours : " + self.selection #Actualiasation de l'affichage de la page en cours dans l'ihm
            self.listbox.delete(0, 'end') #Suppression des liens dans la liste box

            compteurBoucle = 0
            for lien in listeDeLiens: #Remplissage des liens dans la fenêtre en supprimant le début de lien pour la lisibilité
                compteurBoucle += 1
                lien = lien.removeprefix("/wiki/")
                self.listbox.insert(compteurBoucle, lien)
                
        else: #Si jamais la page est en cours et la pageDArrivee sont identiques 
            self.compteur += 1
            self.labelCompteur['text'] = "Compteur de coups : " + str(self.compteur) #Actualisation de l'affiage du compteur dans l'ihm
            self.labelUrl['text'] = "Page en cours : " + self.selection #Actualiasation de l'affichage de la page en cours dans l'ihm
            self.listbox.delete(0, 'end') #Suppression des liens dans la liste box
            print("Bravo vous avez terminé en seulement " + str(self.compteur) + " coups")
            
