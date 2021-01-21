from bs4 import BeautifulSoup
from tkinter import *
import urllib.request
import os
import requests
clear = "\n" * 30
clear = lambda: os.system('cls')
jeuTermine = False
print("Bienvenue dans le jeu de Wikipédia ! ")
print("Le principe est simple, une page de départ et d'arrivée vont être tirée au sort")
print("A vous d'y arriver le plus vite possible")
print("Bonne chance !")
pageDeDepart = ""
pageDArrivee = ""
pageEnCours = ""
compteur = 0

pageDeDepart = 'https://fr.wikipedia.org/wiki/france'
pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

def getHrefFromWikipage():
    listeDeLiens = []

    with urllib.request.urlopen(pageEnCours) as response:
        compteurDeLien = 0
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        print("La page actuelle est : " + soup.find('h1', class_='firstHeading').getText())
        print("Le lien de la page actuelle est : " + soup.select("[rel='canonical']")[0]['href'])
        compteurLiensBons = 0
        compteurLienFaux = 0
        for a in soup.select('.mw-parser-output p a'):
            if any(s in a['href'] for s in ('edit', 'index.php', '#cite_note', 'Citez_vos_sources', 'Ins%C3%A9rer')):
                # print("Mauvais lien : " + 'https://fr.wikipedia.org/' + a['href'])
                compteurLienFaux += 1
            else:
                # print('https://fr.wikipedia.org/' + a['href']
                listeDeLiens.append('https://fr.wikipedia.org/' + a['href'])

        nombreLiensAvantDoublon = len(listeDeLiens)
        listeDeLiens = list(dict.fromkeys(listeDeLiens))

        fenetre = Tk()
        fenetre.geometry("1000x700")

        listbox = Listbox(fenetre, height = 500, width = 300 )
        compteurBoucle = 0

        for b in listeDeLiens:
            # print(b)
            compteurBoucle += 1
            listbox.insert(compteurBoucle, b)
            compteurLiensBons += 1

        listbox.pack()
        fenetre.mainloop()

        print("---------------------------------")
        print("Le total des liens est : " + str((compteurLiensBons + compteurLienFaux)))
        print("Le nombre de bons liens est : " + str(compteurLiensBons))
        print("---------------------------------")
        print("Le nombre de mauvais liens est : " + str(compteurLienFaux))
        print("Le nombre de doublons est : " + str(nombreLiensAvantDoublon - len(listeDeLiens)))


with urllib.request.urlopen(pageDeDepart) as response:

    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')

    pageDeDepart = soup.select("[rel='canonical']")[0]['href']
    pageEnCours = pageDeDepart

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


# while jeuTermine:
clear()
print (clear)
getHrefFromWikipage()
compteur = compteur + 1
