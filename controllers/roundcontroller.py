import datetime
from models import roundmodel
from views import roundview
from controllers import menucontroller


class RoundController:

    def __init__(self):
        self.view = roundview.RoundView()

    def round_creation(self, tournament):
        # generer une nouvelle ronde du tournoi
        new_tour = roundmodel.Round(len(tournament.round_instances),
                                    tournament.id_tournament)
        new_tour.generate_pair(tournament.players, tournament.round_instances)
        tournament.turn.append(new_tour)
        # afficher les résultats de la ronde à jouer
        self.view.display_matches(new_tour)
        new_tour.save_round()
        menucontroller.menu_tournament(tournament, True)

    def round_results(self, tournament):
        tour = tournament.round_instances[len(tournament.round_instances)-1]
        ronde = tournament.turn[len(tournament.turn) - 1]
        for i in range(len(tour)):
            choix = self.view.matches_done(tour, i)
            match_instance = tour[i]
            joueur_1 = match_instance[0]
            joueur_2 = match_instance[1]
            if choix == 1:
                joueur_1[1] += 1
            elif choix == 2:
                joueur_2[1] += 1
            elif choix == 3:
                joueur_1[1] += 0.5
                joueur_2[1] += 0.5
            match = ronde.matches_model[i]
            match.results_player_1 = joueur_1[1]
            match.results_player_2 = joueur_2[1]
            match.maj_results()
        ronde.end_date = datetime.datetime.now()
        ronde.maj_end_date()
        if tournament.turn_number > len(tournament.round_instances):
            menucontroller.menu_tournament(tournament)
        else:
            tournament.tournament_over = True
            tournament.maj_tournament_over()
            menucontroller.end_tournament(tournament)
