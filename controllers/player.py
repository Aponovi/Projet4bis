from controllers import menu
from views import playerranking


class PlayerController:

    def __init__(self):
        self.view = playerranking.Player_RankingView()

    def update_ranking(self, tournament, round_in_progress):
        self.view.update_ranking(tournament)
        tournament.players[self.view.index_player].ranking = self.view.ranking
        menu.menu_tournament(tournament, round_in_progress)
