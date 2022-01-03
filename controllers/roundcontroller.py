import datetime
from models import roundmodel
from views import roundview
from controllers import menucontroller
from tinydb import TinyDB


class RoundController:

    def __init__(self):
        self.view = roundview.RoundView()

    def round_creation(self, tournament):
        serialized_rounds = []
        # generer une nouvelle ronde du tournoi
        new_tour = roundmodel.Round(tournament)
        new_tour.generate_pair(tournament.players, tournament.round_instances)
        tournament.ronde.append(new_tour)
        # afficher les résultats de la ronde à jouer
        self.view.display_matches(new_tour)
        serialized_round = new_tour.serialized_round()
        serialized_rounds.append(serialized_round)
        db = TinyDB('db.json')
        rounds_table = db.table('rounds')
        rounds_table.insert_multiple(serialized_rounds)
        menucontroller.menu_tournament(tournament, True)

    def round_results(self, tournament):
        tour = tournament.round_instances[len(tournament.round_instances)-1]
        for i in range(len(tour)):
            choix = self.view.matches_done(tour, i)
            match = tour[i]
            joueur_1 = match[0]
            joueur_2 = match[1]
            if choix == 1:
                joueur_1[1] += 1
            elif choix == 2:
                joueur_2[1] += 1
            elif choix == 3:
                joueur_1[1] += 0.5
                joueur_2[1] += 0.5
        ronde = tournament.ronde[len(tournament.ronde) - 1]
        ronde.end_date = datetime.datetime.now()
        if tournament.turn_number > len(tournament.round_instances):
            menucontroller.menu_tournament(tournament)
        else:
            tournament.end_date = datetime.datetime.now()
            menucontroller.fin_tournament(tournament)
