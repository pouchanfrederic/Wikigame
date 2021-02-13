from tkinter import *
from utils import *

clear = lambda: os.system('cls')


class Wikigame:

    def __init__(self, fenetre):
        
        self.pageDeDepart = 'https://fr.wikipedia.org/wiki/france'
        # self.pageDeDepart = 'https://fr.wikipedia.org/wiki/Zone_d%27int%C3%A9gration_%C3%A9conomique_r%C3%A9gionale'
        self.pageDArrivee = 'https://fr.wikipedia.org/wiki/guyane'

        # self.pageDeDepart = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
        # self.pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

        self.fenetre = fenetre
        self.fenetre.geometry("600x600")
        self.fenetre.title("Wikigame par Frédéric Pouchan")

        self.pageDeDepart, self.pageDArrivee = initializeVariables(self.pageDeDepart, self.pageDArrivee)
        self.url = self.pageDeDepart
        self.compteur = 0

        self.labelCompteur = Label(self.fenetre, text=("Compteur de coups : " + str(self.compteur)))
        self.labelCompteur.pack()

        self.labelUrl = Label(self.fenetre, text=("Page en cours : " + urllib.parse.unquote(self.url.removeprefix("https://fr.wikipedia.org/wiki/"))))
        self.labelUrl.pack()

        self.label = Label(self.fenetre, text=("Objectif : " + urllib.parse.unquote(self.pageDArrivee.removeprefix("https://fr.wikipedia.org/wiki/"))))
        self.label.pack()

        self.scrollbar = Scrollbar(self.fenetre, orient="vertical")
        self.listbox = Listbox(self.fenetre, width=100, height=40, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.submit = Button(self.fenetre, text='Valider', command=self.updateWindow)
        self.submit.pack()

        self.listbox.pack()

        self.selection = ''

        self.url = self.pageDeDepart

        self.initializeWindow()
        

    def initializeWindow(self):
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

    def updateWindow(self):

        test = self.listbox.curselection()
        if len(test) == 0:
            return
        self.selection = self.listbox.get(self.listbox.curselection())
        
        if ("https://fr.wikipedia.org" + self.selection) != self.pageDArrivee:
            self.compteur += 1
            self.labelCompteur['text'] = "Compteur de coups : " + str(self.compteur) #Actualisation de l'affiage du compteur dans l'ihm
            self.labelUrl['text'] = "Page en cours : " + self.selection #Actualiasation de l'affichage de la page en cours dans l'ihm
            self.listbox.delete(0, 'end') #Suppression des liens dans la liste box

            listeDeLiens = getLinksFromUrl(("https://fr.wikipedia.org/wiki/"+ urllib.parse.quote(self.selection)))
            if len(listeDeLiens) == 0:
                print("La liste de liens est vide")
                return
            compteurBoucle = 0
            for lien in listeDeLiens:
                compteurBoucle += 1
                lien = lien.removeprefix("/wiki/")
                self.listbox.insert(compteurBoucle, lien)
        else:
            print("Bravo vous avez terminé en seulement " + str(self.compteur) + "coups")

    def getPageDeDepart(self):
        return self.pageDeDepart

    def getPageDArrivee(self):
        return self.pageDArrivee

