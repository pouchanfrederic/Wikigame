
from tkinter import *
from utils import *
clear = lambda: os.system('cls')


class Wikigame:

    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.geometry("600x600")
        self.fenetre.title("Wikigame par Frédéric Pouchan")

        self.scrollbar = Scrollbar(self.fenetre, orient="vertical")
        self.listbox = Listbox(self.fenetre, width=100, height=40, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.submit = Button(self.fenetre, text='Submit', command=self.updateWindow)
        self.submit.pack()

        self.listbox.pack()
        
        self.selection = ''
        pageDeDepart = 'https://fr.wikipedia.org/wiki/france'
        self.url = pageDeDepart
        self.initializeWindow()

        self.fenetre.mainloop()

        
    def initializeWindow(self):
        listeDeLiens = getLinksFromUrl(self.url)
        compteurBoucle = 0
        for lien in listeDeLiens:
            compteurBoucle += 1
            self.listbox.insert(compteurBoucle, lien)

    def updateWindow(self):
        self.selection = self.listbox.get(self.listbox.curselection())
        self.listbox.delete(0, 'end')

        listeDeLiens = getLinksFromUrl(self.selection)

        compteurBoucle = 0
        for lien in listeDeLiens:
            compteurBoucle += 1
            self.listbox.insert(compteurBoucle, lien)

        # self.listbox.pack()
