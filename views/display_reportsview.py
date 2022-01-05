class Display_ReportsView:

    def all_players_list(self, players):
        print("\nListe de tous les acteurs : \n")
        for player in players:
            form = f"{player.name:20}{player.first_name:20}{str(player.ranking):20}"
            print(form.format(*players))

    def players_list(self, players, tournament):
        print("\nListe des joueurs : \n")
        for player in players:
            form = f"{player.name:20}{player.first_name:20}{str(player.ranking):20}"
            print(form.format(*players))

    def tournament_list(self, tournaments):
        print("\nListe des tournois : \n")
        for tournament in tournaments:
            form = f"{tournament.name:20}{tournament.place:20}" \
                   f"du {str(tournament.start_date):10} au {str(tournament.end_date):10}"
            print(form.format(*tournaments))

    def round_list(self, rondes):
        for ronde in rondes:
            form = f"{ronde.name:20}" \
                   f"du {str(ronde.start_date):10} au {str(ronde.end_date):10}"
            print(form.format(*rondes))

    def matches_list(self, tournament_id):
        pass

    def tournament_choice(self, tournaments):
        print("\nVeuillez sélectionner un tournoi : \n")
        i = 0
        for tournament in tournaments:
            i += 1
            print(f" {str(i)} {tournament.name}\n")
        choice = -1
        while choice < 0 or choice > len(tournaments):
            choice = input("Votre choix : ")
            try:
                choice = int(choice)
            except ValueError:
                print(f"{choice} n'est pas un nombre!")
                choice = -1
                continue
            if choice > len(tournaments) or choice < 0:
                print("Choix non reconnu.")
                continue
        return tournaments[choice-1].id_tournament.hex
