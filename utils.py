import urllib.request #Permet d'utiliser la librairie urllib, utilisée pour la gestion des accents et autre symboles dans les liens
import os #Permet d'utiliser la fonction cl
from bs4 import BeautifulSoup #Permet d'utiliser la librairie BeautifulSoup

compteurBoucle = 0 #Variable qui permet de remplir la liste de liens
listeDeLiens = '' #Variable qui contient tous les liens présents dans une page
urlDeSecours = '' #Variable qui stock l'url de secours, utilisée si la page de départ est vide
url = '' #Variable qui stock l'url de la page en cours


def initializeVariables(pageDeDepart, pageDArrivee):  #Méthode qui permet de récupèrer l'url de la page de départ et d'arrivée

    with urllib.request.urlopen(pageDeDepart) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser') #Variable qui contient toutes les données de la page

        pageDeDepart = soup.select("[rel='canonical']")[0]['href']  #Permet de récupérer l'url de la page de départ, en filtrant sur le nom de la class et le type de balise

        # nomDeLaPageDeDepart = soup.find('h1', class_='firstHeading') #Autre manière de trouver le nom de la page de départ

    with urllib.request.urlopen(pageDArrivee) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser') #Variable qui contient toutes les données de la page
        pageDArrivee = soup.select("[rel='canonical']")[0]['href'] #Permet de récupérer l'url de la page d'arrivée, en filtrant sur le nom de la class et le type de balise

        # nomDeLaPageDArrivee = soup.find('h1', class_='firstHeading') #Autre manière de trouver le nom de la page d'arrivée

        return pageDeDepart, pageDArrivee #Permet de récupérer le nom de la page de départ et d'arrivée


def getLinksFromUrl(url): #Méthode qui permet de filtrer puis récupèrer les liens de la page en cours
    listeDeLiens = [] #Variable qui contient tous les liens présents dans une page
    try: #Permet la gestion d'éxception au sein de la méthode
        with urllib.request.urlopen(url) as response:
            webpage = response.read()
            soup = BeautifulSoup(webpage, 'html.parser') #Variable qui contient toutes les données de la page
            print("La page actuelle est : " + soup.find('h1', class_='firstHeading').getText()) #Permet de savoir dans la console le nom de la page en cours dans la console
            print("Le lien de la page actuelle est : " + soup.select("[rel='canonical']")[0]['href']) #Permet de savoir le lien de la page en cours dans la console
            global urlDeSecours #Cette ligne permet d'utiliser la variable globale urlDeSecours
            urlDeSecours = soup.select("[rel='canonical']")[0]['href']  # Cette variable est utilisée dans le cas où la page générée ne contient pas de liens
            for a in soup.select('.mw-parser-output p a'): #boucle qui permet de filtrer le type de liens récupérer par l'application
                if any(s in a['href'] for s in ('edit', 'index.php', '#cite_note', 'Citez_vos_sources', 'Ins%C3%A9rer', 'donate', 'API_', 'Aide','Wikidata', 'Wiktionary')):
                    pass #Aucun traitement si le lien contient un des mots ci-dessus, donc on ne traite pas ce cas, ces liens ne sont pas utilisables
                else: #Si les liens ne contiennent pas le texte indiqué dans le if :
                    listeDeLiens.append(urllib.parse.unquote(a['href'])) #Le lien est ajouté à la liste de liens, en enlevant tous les accents et autres symboles, grâce à la librairie
            listeDeLiens = list(dict.fromkeys(listeDeLiens)) #Ajout de la liste de liens dans un dictionnaire, pour supprimer tous les liens présents en double, car 
            #un dictionnaire ne peut contenir de doublons
            return listeDeLiens #Permet de récupérer la listeDeLiens avec tous les liens
    except: #Dans le cas où une erreur intervient, cela concerne le cas où une page est vide
        print("La page est vide") #Erreur affichée dans la console
        return listeDeLiens #Renvoie une liste de liens vide, pour que le reste de l'application puisse récupèrer la variable dans tous les cas 




def getUrlDeSecours():  # Gestion au cas où la page première page serait une page vide
    return urllib.parse.unquote(urlDeSecours.removeprefix("https://fr.wikipedia.org/wiki/")) #RemovePrefix permet de supprimer une partie d'une string, ici le début du lien
