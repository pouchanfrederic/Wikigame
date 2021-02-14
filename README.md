# Wikigame

Jeu basé sur le célèbre site Wikipedia. 
Le principe est simple, l'application génère aléatoirement une page de départ et une page d'arrivée.
Le but est de se rendre sur la page d'arrivée le plus rapidement possible.
Amusez-vous bien ! 

# Librairies utilisées : 
- urllib
- BeautifulSoup (pour l'installer : pip install beautifulsoup4)
- utils
- tkinter

# Fonctionnalités : 
- Tri de liens intelligent (Pas de doublons, ni de liens indésirables).
- Si la page de départ ne contient pas de lien, un nouveau est générée automatiquement.
- Si la page sélectionnée par l'utilisateur est vide, l'application ne s'actualise pas, pour que celui-ci ne se retrouve pas bloqué.
- Le jeu compte le nombre de coup jusqu'à atteindre la "ligne d'arrivée"
