class Display_ReportsView:

    @staticmethod
    def all_players_list(players):
        print("\nListe de tous les acteurs : \n")
        for player in players:
            form = f"{player.name:20}" \
                   f"{player.first_name:20}{str(player.ranking):20}"
            print(form.format(*players))

    @staticmethod
    def players_list(players):
        print("\nListe des joueurs du tournoi: \n")
        for player in players:
            form = f"{player.name:20}" \
                   f"{player.first_name:20}{str(player.ranking):20}"
            print(form.format(*players))

    @staticmethod
    def tournament_list(tournaments):
        print("\nListe des tournois : \n")
        for tournament in tournaments:
            form = f"{tournament.name:20}{tournament.place:20}" \
                   f"du {str(tournament.start_date):10} " \
                   f"au {str(tournament.end_date):10}"
            print(form.format(*tournaments))

    @staticmethod
    def round_list(rondes):
        for ronde in rondes:
            form = f"{ronde.name:20}" \
                   f"du {str(ronde.start_date):10} au {str(ronde.end_date):10}"
            print(form.format(*rondes))

    @staticmethod
    def matches_list(matches):
        print("\nListe des matches : \n")
        for match in matches:
            if match.results_player_1 == 1:
                results_match = f"Victoire {match.player_1.name}"
            elif match.results_player_2 == 1:
                results_match = f"Victoire {match.player_2.name}"
            elif match.results_player_1 == 0.5 \
                    and match.results_player_2 == 0.5:
                results_match = "Match nul"
            else:
                results_match = "Match non joué"
            form = f"{str(match.player_1.name):10}" \
                   f"{str(match.player_1.first_name):10}   vs   " \
                   f"{str(match.player_2.name):10}" \
                   f"{str(match.player_2.first_name):10}" \
                   f"   Résultat : {results_match}"
            print(form.format(*matches))

    @staticmethod
    def tournament_choice(tournaments):
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
        return tournaments[choice - 1].id_tournament.hex
