from models import roundmodel
from views import roundview


class RoundController:

    def __init__(self):
        self.view = roundview.RoundView()

    def round_creation(self, tournament):
        # generer une nouvelle ronde du tournoi
        new_tour = roundmodel.Round(tournament)
        new_tour.generate_pair(tournament.players, tournament.round_instances)
        # afficher les résultats de la ronde à jouer
        self.view.display_matches(new_tour)


    def round_results(self, tournament):
