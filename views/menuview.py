from controllers import tournamentcontroller


def welcome():
    """ Message d'accueil du programme """
    print('\n')
    print("Gestionnaire de tournoi d'échecs")
    print("Veuillez entrer le numéro correspondant à l'action voulue.\n")


def main_menu():
    """Menu permettant à l'utilisateur de choisir de : créer un tournoi, mettre à jour les classement ou afficher les
    rapports """
    print("Menu principal:\n")
    print("1 : Créer un nouveau tournoi")
    print("2 : Afficher les rapports")
    print("\n3 : TEST Tournoi\n")

    choice = -1
    while choice < 0 or choice > 3:
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"{choice} n'est pas un nombre!")
            choice = -1
            continue
        if choice > 3 or choice < 0:
            print("Choix non reconnu.")
            continue
    return choice


def tournament_menu(round_in_progress=False):
    print("\nMenu Tournoi:\n")
    if not round_in_progress:
        print("1 : Générer une ronde.")
    else:
        print("1 : Saisir les scores de la ronde en cours")
    print("2 : Mettre à jour les classements.\n")

    choice = -1
    while choice < 0 or choice > 2:
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Choix non reconnu.")
            choice = -1
            continue
        if choice > 2 or choice < 0:
            print("Choix non reconnu.")
            continue
    return choice

def reports_menu():
    print("Menu rapports:\n")
    print("1 : Retourner au menu principal.")
    print("2 : Liste de tous les acteurs par ordre alphabétique")
    print("3 : Liste de tous les acteurs par classement")
    print("4 : Liste de tous les joueurs d'un tournoi par ordre alphabétique")
    print("5 : Liste de tous les joueurs d'un tournoi par classement")
    print("6 : Liste de tous les tournois")
    print("7 : Liste de tous les tours d'un tournoi")
    print("8 : Liste de tous les matchs d'un tournoi")

    choice = -1
    while choice < 0 or choice > 8:
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"{choice} n'est pas un nombre!")
            choice = -1
            continue
        if choice > 8 or choice < 0:
            print("Choix non reconnu.")
            continue
    return choice
