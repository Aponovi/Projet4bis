from controllers import menu
from views import check


class TournamentView:

    def __init__(self):
        self.name = ""
        self.place = ""
        self.start_date = None
        self.end_date = None
        self.time_control = None
        self.nb_players = 8
        self.nb_rounds = 4
        self.description = ""

    def new_tournament(self):
        print("\nCréation d'un tournoi:\n")
        self.name = check\
            .field_string("Veuillez saisir le nom du tournoi: ", isalnum=True)
        self.place = check\
            .field_string("Veuillez saisir le lieu du tournoi: ", isalnum=True)
        date_error = True
        self.start_date = None
        self.end_date = None
        while date_error:
            self.start_date = check\
                .field_date("Veuillez saisir la date de début du tournoi ("
                            "jj/mm/aaaa): ")
            self.end_date = check\
                .field_date("Veuillez saisir la date de fin du tournoi ("
                            "jj/mm/aaaa): ")
            if self.start_date <= self.end_date:
                date_error = False
            else:
                print('La date de début du tournoi doit être antérieure à la '
                      'date de fin.')
        self.time_control = time_choice()
        self.nb_players = check\
            .field_int("Veuillez saisir le nombre de joueurs: ")
        self.nb_rounds = check\
            .field_int("Veuillez saisir le nombre de tours: ")
        self.description = check\
            .field_string("Description du tournoi: ", max_len=1000)
        return (self.name,
                self.place,
                self.start_date,
                self.end_date,
                self.time_control,
                self.description,
                self.nb_players,
                self.nb_rounds)


def time_choice():
    print("Veuillez choisir le mode de contrôle du temps du tournoi: ")
    print("1 : Bullet.")
    print("2 : Blitz.")
    print("3 : Coup rapide.")
    choice = -1
    while choice < 0 or choice > 3:
        choice = input("Votre choix : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Choix non reconnu.")
            choice = -1
            continue
        if choice > 3 or choice < 0:
            print("Choix non reconnu.")
            continue
    if choice == 1:
        return "Bullet"
    elif choice == 2:
        return "Blitz"
    elif choice == 3:
        return "Coup rapide"
    else:
        return ""


def tournament_players(in_tournament):
    print("\nCréation d'un joueur:\n")
    name = check\
        .field_string("Veuillez saisir le nom du joueur: ", isalpha=True)
    first_name = check\
        .field_string("Veuillez saisir le prénom du joueur: ", isalpha=True)
    birth_date = check\
        .field_date("Veuillez saisir la date de naissance du joueur ("
                    "jj/mm/aaaa): ")
    gender = check\
        .check_gender("Veuillez saisir le genre du joueur (f/m): ")
    ranking = check\
        .field_int("Veuillez saisir le classement du joueur: ")
    return in_tournament, name, first_name, birth_date, gender, ranking


def fin_tournoi_affichage(players=None):
    if players is None:
        players = []
    print("\nLes résultats du tournoi sont: \n")
    for player in players:
        score = player[1]
        name = player[0].name
        first_name = player[0].first_name
        print(f"{name} {first_name} : {score} points")
    menu.start_program()
