from controllers import menucontroller
from models import playermodel, tournamentmodel
from views import display_reportsview


class ReportsController:
    def __init__(self):
        self.view = display_reportsview.Display_ReportsView()

    def all_players_list_by_alpha_order(self):
        players = playermodel.Player.load_players()
        self.view.all_players_list(players)
        menucontroller.start_program()

    def all_players_list_by_ranking_order(self):
        players = playermodel.Player.load_players(True)
        self.view.all_players_list(players)
        menucontroller.start_program()

    def tournament_players_list_by_alpha_order(self):
        pass

    def tournament_players_list_by_ranking_order(self):
        pass

    def tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        self.view.tournament_list(tournaments)
        menucontroller.start_program()

    def rounds_tournaments_list(self):
        pass

    def matches_tournaments_list(self):
        pass
