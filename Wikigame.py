from tkinter import *
from utils import *

clear = lambda: os.system('cls')


class Wikigame:

    def __init__(self, fenetre):
        self.pageDeDepart = 'https://fr.wikipedia.org/wiki/france'
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

        self.labelUrl = Label(self.fenetre, text=("Page en cours : " + self.url))
        self.labelUrl.pack()

        self.label = Label(self.fenetre, text=("Objectif : " + self.pageDArrivee))
        self.label.pack()

        self.scrollbar = Scrollbar(self.fenetre, orient="vertical")
        self.listbox = Listbox(self.fenetre, width=100, height=40, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.submit = Button(self.fenetre, text='Submit', command=self.updateWindow)
        self.submit.pack()

        self.listbox.pack()

        self.selection = ''


        self.url = self.pageDeDepart

        self.initializeWindow()



    def initializeWindow(self):
        listeDeLiens = getLinksFromUrl(self.url)  # Tous les liens de page liée à l'url donnée en paramètre
        compteurBoucle = 0
        for lien in listeDeLiens:
            compteurBoucle += 1
            self.listbox.insert(compteurBoucle, lien)

    def updateWindow(self):

        test = self.listbox.curselection()
        if len(test) == 0:
            return
        self.selection = self.listbox.get(self.listbox.curselection())
        if self.selection != self.pageDArrivee:

            self.compteur += 1
            self.labelCompteur['text'] = "Compteur de coups : " + str(self.compteur)
            self.labelUrl['text'] = "Page en cours : " + self.selection
            self.listbox.delete(0, 'end')

            listeDeLiens = getLinksFromUrl(self.selection)

            compteurBoucle = 0
            for lien in listeDeLiens:
                compteurBoucle += 1
                self.listbox.insert(compteurBoucle, lien)
        else:
            print("Bravo vous avez terminé en seulement " + str(self.compteur) + "coups")

        # self.listbox.pack()

    def getPageDeDepart(self):
        return self.pageDeDepart

    def getPageDArrivee(self):
        return self.pageDArrivee
