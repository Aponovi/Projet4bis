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

    def matches_done(self, tour):
        pass
