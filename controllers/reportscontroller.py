from controllers import menucontroller
from models import playermodel, tournamentmodel, roundmodel, matchmodel
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
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        players = playermodel.Player.load_players()
        id_tournament = self.view.tournament_choice(tournaments)
        players_tournament = []
        for i in range(len(players)):
            if players[i].id_tournament == id_tournament:
                players_tournament.append(players[i])
        self.view.players_list(players_tournament, tournaments)
        menucontroller.start_program()

    def tournament_players_list_by_ranking_order(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        players = playermodel.Player.load_players(True)
        id_tournament = self.view.tournament_choice(tournaments)
        players_tournament = []
        for i in range(len(players)):
            if players[i].id_tournament == id_tournament:
                players_tournament.append(players[i])
        self.view.players_list(players_tournament, tournaments)
        menucontroller.start_program()

    def tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        self.view.tournament_list(tournaments)
        menucontroller.start_program()

    def rounds_tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        id_tournament = self.view.tournament_choice(tournaments)
        rondes = roundmodel.Round.load_round()
        rondes_tournament = []
        for i in range(len(rondes)):
            if rondes[i].id_tournament.hex == id_tournament:
                rondes_tournament.append(rondes[i])
        self.view.round_list(rondes_tournament)
        menucontroller.start_program()

    def matches_tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        id_tournament = self.view.tournament_choice(tournaments)
        matches = matchmodel.Match.load_match()
        matches_tournament = []
        for i in range(len(matches)):
            if matches[i].id_tournament.hex == id_tournament:
                matches_tournament.append(matches[i])
        self.view.round_list(matches_tournament)
        menucontroller.start_program()

