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
        self.view.players_list(players_tournament)
        menucontroller.start_program()

    def tournament_players_list_by_ranking_order(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        players = playermodel.Player.load_players(True)
        id_tournament = self.view.tournament_choice(tournaments)
        players_tournament = []
        for i in range(len(players)):
            if players[i].id_tournament == id_tournament:
                players_tournament.append(players[i])
        self.view.players_list(players_tournament)
        menucontroller.start_program()

    def tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        self.view.tournament_list(tournaments)
        menucontroller.start_program()

    def rounds_tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        id_tournament = self.view.tournament_choice(tournaments)
        rounds = roundmodel.Round.load_round()
        rounds_tour = []
        for i in range(len(rounds)):
            if rounds[i].id_tournament.hex == id_tournament:
                rounds_tour.append(rounds[i])
        self.view.round_list(rounds_tour)
        menucontroller.start_program()

    def matches_tournaments_list(self):
        tournaments = tournamentmodel.TournamentModel.load_tournaments()
        id_tournament = self.view.tournament_choice(tournaments)
        matches = matchmodel.Match.load_match()
        matches_tournament = []
        rounds = roundmodel.Round.load_round()
        round_tour = []
        for i in range(len(rounds)):
            if rounds[i].id_tournament.hex == id_tournament:
                round_tour.append(rounds[i])
        for k in range(len(matches)):
            for j in range(len(round_tour)):
                if matches[k].id_round.hex == round_tour[j].id_round.hex:
                    matches_tournament.append(matches[k])
        self.view.matches_list(matches_tournament)
        menucontroller.start_program()
