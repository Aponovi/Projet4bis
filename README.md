# Projet 4 - Application de tournois d'échecs

Il s'agit d'une application en Python lancée depuis la console.

L'application permet de gérer des tournois d'échecs selon le système de tournois "Suisse".

## INSTALLATION ET EXECUTION DU PROGRAMME

### Installation et exécution de l'application avec pipenv
1. Cloner ce dépôt de code à l'aide de la commande `$ git clone clone https://github.com/Aponovi/Projet4bis.git` (vous pouvez également télécharger le code en temps qu'archive zip)
2. Rendez-vous depuis un terminal à la racine du répertoire Projet4bis avec la commande `$ cd Projet4bis`
3. Installez les dépendances du projet à l'aide de la commande `pipenv install`
4. Lancer le programme avec `python main.py`

### Installation et exécution de l'application sans pipenv (avec venv et pip)
1. Cloner ce dépôt de code à l'aide de la commande `$ git clone clone https://github.com/Aponovi/Projet4bis.git` (vous pouvez également télécharger le code en temps qu'archive zip)
2. Rendez-vous depuis un terminal à la racine du répertoire Projet4bis avec la commande `$ cd Projet4bis`
3. Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`
6. Lancer le programme avec `python main.py`


## UTILISATION DU PROGRAMME

### DEROULEMENT DE BASE DU TOURNOI

Voici comment s'organise un tournoi d'échecs :

    1. Créer un nouveau tournoi (option 1)
    - saisir le nom du tournoi
    - saisir le lieu du tournoi
    - saisir la date de début du tournoi (jj/mm/aaaa)
    - saisir la date de fin du tournoi (jj/mm/aaaa)
    - choisir le mode de contrôle du temps du tournoi
    - saisir le nombre de joueurs
    - saisir le nombre de tours
    - saisir la description du tournoi
    
    2. Créer les joueurs selon le modèle :
            • Nom de famille
            • Prénom
            • Date de naissance
            • Sexe
            • Classement
    
    3. Générer une ronde (option 1) :
        Affichage des matchs à jouer
    
    4. Lorsque le tour est terminé, saisir les résultats (option 1)
    
    5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.
   
 Il est possible de quitter le programme entre les tours grâce à l'option "quitter le programme" (choix 3 du menu Tournoi et choix 3 du menu principal).
 
 La sauvegarde se fait au fur et à mesure et le chargement est automatique lorsque le programme est relancé.
 
### METTRE A JOUR LES CLASSEMENTS

A tout moment du tournoi grace à l'option "Mettre à jour les classements (choix 2 du menu Tournoi):

     1.Saisir le numéro du joueur dont le classement est à modifier
     2.Les nom, prénom et classment du joueur s'affichent dans la console pour vérification. Saisir le nouveau classement et appuyer sur "entrée".
     
 ### GENERER DES RAPPORTS  
 
 Afficher le menu rapports (option 2 du menu principal) :
 
  1. Retourner au menu principal.
  2. Liste de tous les acteurs par ordre alphabétique
  3. Liste de tous les acteurs par classement
  4. Liste de tous les joueurs d'un tournoi par ordre alphabétique
  5. Liste de tous les joueurs d'un tournoi par classement
  6. Liste de tous les tournois
  7. Liste de tous les tours d'un tournoi
  8. Liste de tous les matchs d'un tournoi
 
 Saisir le numéro de l'option choisie, le rapport généré s'affiche dans la console.
 
 
## GENERER UN RAPPORT FLAKE8 HTML

  1.Rendez-vous depuis un terminal à la racine du répertoire Projet4bis avec la commande `$ cd Projet4bis`  
  2.Générer un nouveau rapport avec `$ flake8 --format=html --htmldir=flake8_rapport`
  3.Consulter le rapport qui se situe dans le dossier "flake8_rapport" en ouvrant "index.html".
