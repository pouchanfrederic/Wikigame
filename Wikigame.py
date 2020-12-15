from bs4 import BeautifulSoup
import urllib.request
import requests
print("Bienvenue dans le jeu de Wikipédia ! ")
print("Le principe est simple, une page de départ et d'arrivée vont être tirée au sort")
print("A vous d'y arriver le plus vite possible")
print("Bonne chance !")
pageDeDepart = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
pageDArrivee = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

with urllib.request.urlopen(pageDeDepart) as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    pageDeDepart = soup.select("[rel='canonical']")[0]['href']
    print("Vous commencez de la page : " + pageDeDepart)

with urllib.request.urlopen(pageDArrivee) as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    pageDArrivee = soup.select("[rel='canonical']")[0]['href']
    print("Vous devez arriver à la page : " + pageDArrivee)