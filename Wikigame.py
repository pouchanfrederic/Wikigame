from bs4 import BeautifulSoup
import urllib.request
import os
import requests
clear = "\n" * 30
clear = lambda: os.system('cls') #Todo virer ce clear
jeuTermine = False
print("Bienvenue dans le jeu de Wikipédia ! ")
print("Le principe est simple, une page de départ et d'arrivée vont être tirée au sort")
print("A vous d'y arriver le plus vite possible")
print("Bonne chance !")

pageDeDepart = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

def getHrefFromWikipage():
    with urllib.request.urlopen(pageEnCours) as response:
        compteurDeLien = 0
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        print("La page actuelle est : " + soup.find('h1', class_='firstHeading').getText())
        print("Le lien de la page actuelle est : " + soup.select("[rel='canonical']")[0]['href'])
    if pageEnCours != pageDArrivee:
        for a in soup.select('.mw-parser-output p a'):
            # Ceci est une modification pour faire un test
            if any(s in a['href'] for s in ('edit', 'index.php', '#cite_note', 'Citez_vos_sources', 'Ins%C3%A9rer')):
                print('-------- MAUVAIS LIEN DONC SUPPRIME --------')
            else:
                print(a['href'])
        compteurDeLien = compteurDeLien +1
    else:
        jeuTermine = True
        print("Bravo vous avez terminé en seulement " & compteur & "coups")


with urllib.request.urlopen(pageDeDepart) as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    pageDeDepart = soup.select("[rel='canonical']")[0]['href']
    pageEnCours = pageDeDepart #Todo : Page en cours doit être égal à la saisie utilisateur
    nomDeLaPageDeDepart = soup.find('h1', class_ ='firstHeading')
    print("Vous commencez de la page : " + pageDeDepart)
    print("Le nom de la page de départ est : " + nomDeLaPageDeDepart.getText())


with urllib.request.urlopen(pageDArrivee) as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    pageDArrivee = soup.select("[rel='canonical']")[0]['href']
    nomDeLaPageDArrivee = soup.find('h1', class_ ='firstHeading')
    print("Vous devez arriver à la page : " + pageDArrivee)
    print("Le nom de la page d'arrivée est : " + nomDeLaPageDArrivee.getText())


while jeuTermine:
    clear()
    print (clear)
    getHrefFromWikipage()
    compteur = compteur + 1