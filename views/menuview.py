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
    print("1 : Créer un nouveau tournoi.")
    print("2 : Mettre à jour les classements.")
    print("3 : Afficher les rapports\n")
    print("4 : TEST Tournoi\n")

    choice = -1
    while choice < 0 or choice > 4:
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"{choice} n'est pas un nombre!")
            choice = -1
            continue
        if choice > 4 or choice < 0:
            print("Choix non reconnu.")
            continue
    return choice


def tournament_menu(round_in_progress=False):
    print("Menu Tournoi:\n")
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
