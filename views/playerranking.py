from views import check


class Player_RankingView:

    def __init__(self):
        self.ranking = -1
        self.index_player = -1

    def update_ranking(self, tournament):
        for i in range(len(tournament.players)):
            print(str(i) + " : " + tournament.players[i].name
                  + " " + tournament.players[i].first_name
                  + " (" + str(tournament.players[i].ranking) + ")")
        self.index_player = -1
        while self.index_player < 0 \
                or self.index_player >= len(tournament.players):
            self.index_player = input("Veuillez sélectionner le joueur à "
                                      "mettre à jour: ")
            try:
                self.index_player = int(self.index_player)
            except ValueError:
                print("Choix non reconnu.")
                self.index_player = -1
                continue
            if self.index_player < 0 \
                    or self.index_player >= len(tournament.players):
                print("Choix non reconnu.")
                continue
        print(tournament.players[self.index_player].name
              + " " + tournament.players[self.index_player].first_name
              + " (" + str(tournament.players[self.index_player].ranking)
              + ")")
        self.ranking = -1
        while self.ranking < 0:
            self.ranking = check \
                .field_int("Veuillez saisir le nouveau classement: ")
