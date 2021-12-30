from controllers import menucontroller
from views import player_rankingview


class PlayerController:

    def __init__(self):
        self.view = player_rankingview.Player_RankingView()

    def update_ranking(self, tournament, round_in_progress):
        self.view.update_ranking(tournament)
        tournament.players[self.view.index_player].ranking = self.view.ranking
        menucontroller.menu_tournament(tournament, round_in_progress)
