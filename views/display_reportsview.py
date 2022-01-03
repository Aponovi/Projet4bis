class Display_ReportsView:

    def all_players_list(self, players):
        print("\nListe des joueurs : \n")
        for player in players:
            print(f" {player.name} {player.first_name} {str(player.ranking)}")

    def players_list(self, tournament):
        pass

    def tournament_list(self, tournaments):
        print("\nListe des tournois : \n")
        for tournament in tournaments:
            print(tournament.name)

    def round_list(self, tournament):
        pass

    def matches_list(self, tournament):
        pass
