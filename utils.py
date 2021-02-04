import urllib.request
import os
from bs4 import BeautifulSoup
clear = lambda: os.system('cls')
compteur = 0
compteurBoucle = 0
listeDeLiens = ''
pageDeDepart = 'https://fr.wikipedia.org/wiki/france'
url = pageDeDepart
pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

def getLinksFromUrl(url):
    global compteur
    compteur = compteur + 1
    listeDeLiens = []
    with urllib.request.urlopen(url) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        print("La page actuelle est : " + soup.find('h1', class_='firstHeading').getText())
        print("Le lien de la page actuelle est : " + soup.select("[rel='canonical']")[0]['href'])
        compteurLienFaux = 0
        if url != pageDArrivee:
            for a in soup.select('.mw-parser-output p a'):
                if any(s in a['href'] for s in ('edit','index.php','#cite_note','Citez_vos_sources', 'Ins%C3%A9rer', 'donate', 'API_')):
                    compteurLienFaux += 1
                else:
                    listeDeLiens.append('https://fr.wikipedia.org/' + a['href'])
            listeDeLiens = list(dict.fromkeys(listeDeLiens))
            return listeDeLiens
        else:
            jeuTermine = True
            print("Bravo vous avez terminé en seulement " & compteur & "coups")
            return jeuTermine

def initializeVariables():
    global pageDeDepart
    global pageDArrivee
    global url

    with urllib.request.urlopen(pageDeDepart) as response:

        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')

        pageDeDepart = soup.select("[rel='canonical']")[0]['href']

        # container = soup.find_all("div", attrs={'class': 'mw-parser-output'})
        # resumeParagrahe = container.find("p").getText()
        # print(resumeParagrahe)

        nomDeLaPageDeDepart = soup.find('h1', class_='firstHeading')

    with urllib.request.urlopen(pageDArrivee) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        pageDArrivee = soup.select("[rel='canonical']")[0]['href']

        # container2 = soup.find("div", attrs={'class': 'mw-parser-output'})
        # resumeParagraphe2 = container2.find_all("p")
        # print(resumeParagraphe2)

        nomDeLaPageDArrivee = soup.find('h1', class_='firstHeading')
