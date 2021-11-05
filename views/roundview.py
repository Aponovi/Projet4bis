class RoundView:

    def __init__(self):
        self.name = None
        self.start_date = None
        self.end_date = None
        self.matches = None

    def display_matches(self, new_tour):
        print("les matches sont les suivants : ")
        for i in range(len(new_tour.matches)):
            match = new_tour.matches[i]
            joueur_1 = match[0]
            joueur_2 = match[1]
            to_print = joueur_1[0].first_name
            to_print += " " + joueur_1[0].name
            to_print += " (classement : " + str(joueur_1[0].ranking) + ")"
            to_print += " VS " + joueur_2[0].first_name
            to_print += " " + joueur_2[0].name
            to_print += " (classement : " + str(joueur_2[0].ranking) + ")"

            print(to_print)

    def matches_done(self, tour, num_match):
        match = tour[num_match]
        joueur_1 = match[0]
        joueur_2 = match[1]
        name_player_one = joueur_1[0].first_name + " " + joueur_1[0].name
        name_player_two = joueur_2[0].first_name + " " + joueur_2[0].name
        print("Saisir le résultat du match :")
        print("1 : Vainqueur " + name_player_one)
        print("2 : Vainqueur " + name_player_two)
        print("3 : Match nul")

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

