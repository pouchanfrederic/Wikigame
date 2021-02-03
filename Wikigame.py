from bs4 import BeautifulSoup
from tkinter import *
import urllib.request
import os
import requests

clear = lambda: os.system('cls')
jeuTermine = False

print("Bienvenue dans le jeu de Wikipédia ! ")
print("Le principe est simple, une page de départ et d'arrivée vont être tirée au sort")
print("A vous d'y arriver le plus vite possible")
print("Bonne chance !")

compteur = 0

pageDeDepart = 'https://fr.wikipedia.org/wiki/france'
pageEnCours = pageDeDepart
pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

def getHrefFromWikipage(self):
    listeDeLiens = []
    with urllib.request.urlopen(pageEnCours) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        print("La page actuelle est : " + soup.find('h1', class_='firstHeading').getText())
        print("Le lien de la page actuelle est : " + soup.select("[rel='canonical']")[0]['href'])
        compteurLiensBons = 0
        compteurLienFaux = 0
        if pageEnCours != pageDArrivee:
            for a in soup.select('.mw-parser-output p a'):
                if any(s in a['href'] for s in ('edit','index.php','#cite_note','Citez_vos_sources', 'Ins%C3%A9rer', 'donate')):
                    # print("Mauvais lien : " + 'https://fr.wikipedia.org/' + a['href'])
                    compteurLienFaux += 1
                else:
                    # print('https://fr.wikipedia.org/' + a['href']
                    listeDeLiens.append('https://fr.wikipedia.org/' + a['href'])

            nombreLiensAvantDoublon = len(listeDeLiens)
            listeDeLiens = list(dict.fromkeys(listeDeLiens))

            fenetre = Tk()
            fenetre.geometry("600x600")
            fenetre.title("Wikigame par Frédéric Pouchan")
            
            scrollbar = Scrollbar(fenetre, orient="vertical")
            listbox = Listbox(fenetre, width=100, height=40, yscrollcommand=scrollbar.set)
            
            scrollbar.config(command=listbox.yview)
            scrollbar.pack(side="right", fill="y")
            
            compteurBoucle = 0

            for b in listeDeLiens:
                # print(b)
                compteurBoucle += 1
                listbox.insert(compteurBoucle, b)
                compteurLiensBons += 1

            def submitButton():
                selection = listbox.get(listbox.curselection())
                pageEnCours = selection
                getHrefFromWikipage()

            submit = Button(fenetre, text='Submit', command=submitButton)
            submit.pack()
            listbox.pack()

            fenetre.mainloop()

            print("---------------------------------")
            print("Le total des liens est : " + str((compteurLiensBons + compteurLienFaux)))
            print("Le nombre de bons liens est : " + str(compteurLiensBons))
            print("---------------------------------")
            print("Le nombre de mauvais liens est : " + str(compteurLienFaux))
            print("Le nombre de doublons est : " + str(nombreLiensAvantDoublon - len(listeDeLiens)))
        else:
            jeuTermine = True
            return jeuTermine
            print("Bravo vous avez terminé en seulement " & compteur & "coups")

def initializeVariables(self):
    with urllib.request.urlopen(pageDeDepart) as response:

        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')

        pageDeDepart = soup.select("[rel='canonical']")[0]['href']

        # container = soup.find_all("div", attrs={'class': 'mw-parser-output'})
        # resumeParagrahe = container.find("p").getText()
        # print(resumeParagrahe)

        nomDeLaPageDeDepart = soup.find('h1', class_='firstHeading')
        print("Vous commencez de la page : " + pageDeDepart)
        print("Le nom de la page de départ est : " + nomDeLaPageDeDepart.getText())


    with urllib.request.urlopen(pageDArrivee) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        pageDArrivee = soup.select("[rel='canonical']")[0]['href']

        # container2 = soup.find("div", attrs={'class': 'mw-parser-output'})
        # resumeParagraphe2 = container2.find_all("p")
        # print(resumeParagraphe2)

        nomDeLaPageDArrivee = soup.find('h1', class_='firstHeading')
        print("Vous devez arriver à la page : " + pageDArrivee)
        print("Le nom de la page d'arrivée est : " + nomDeLaPageDArrivee.getText())
        print("---------------------------------------------------------------------------------------------------")


# while not jeuTermine:
initializeVariables()
clear()
getHrefFromWikipage()
compteur = compteur + 1
