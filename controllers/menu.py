import sys

from models import player as player_m, round as round_m, tournament as tour_m
from views import menu, \
    tournament as tour_v
from controllers import player as player_c,\
    round as round_c, \
    tournament as tour_c, \
    reports


def start_program():
    tour = tour_m.TournamentModel.load_last_tournament()
    if tour is not None:
        tour.players = player_m \
            .Player.load_players_by_tournament(tour.id_tournament)
        tour.turn = round_m \
            .Round.load_round_by_tour(tour.id_tournament)
        round_instances = []
        i = 1
        last_match_completed = False
        if len(tour.turn) == 0:
            last_match_completed = True
        for turn in tour.turn:
            turn.load_match_by_turn()
            turn.matches = []
            for match in turn.matches_model:
                turn.matches.append(match.match_tuple())
                if i == len(tour.turn):
                    if match.results_player_1 != 0:
                        last_match_completed = True
            round_instances.append(turn.matches)
            i += 1
        tour.round_instances = round_instances
        menu_tournament(tour, not last_match_completed)
    menu.welcome()
    choice = menu.main_menu()

    if choice == 1:
        controller_tournament = tour_c.TournamentController()
        controller_tournament.tournament_creation()

    elif choice == 2:
        controller_reports = reports.ReportsController()
        choice_reports = menu.reports_menu()
        if choice_reports == 1:
            start_program()

        elif choice_reports == 2:
            controller_reports.all_players_list_by_alpha_order()

        elif choice_reports == 3:
            controller_reports.all_players_list_by_ranking_order()

        elif choice_reports == 4:
            controller_reports.tournament_players_list_by_alpha_order()

        elif choice_reports == 5:
            controller_reports.tournament_players_list_by_ranking_order()

        elif choice_reports == 6:
            controller_reports.tournaments_list()

        elif choice_reports == 7:
            controller_reports.rounds_tournaments_list()

        elif choice_reports == 8:
            controller_reports.matches_tournaments_list()

    elif choice == 3:
        bye_bye()

    elif choice == 4:
        controller_tournament = tour_c.TournamentController()
        controller_tournament.tournament_creation_test()


def menu_tournament(tour, round_in_progress=False):
    choice = menu.tournament_menu(round_in_progress)
    if choice == 1:
        if not round_in_progress:
            """Générer une ronde"""
            round_controller = round_c.RoundController()
            round_controller.round_creation(tour)
        else:
            """Saisir les scores de la ronde"""
            round_controller = round_c.RoundController()
            round_controller.round_results(tour)
    elif choice == 2:
        """Mettre à jour classement"""
        player_controller = player_c.PlayerController()
        player_controller.update_ranking(tour, round_in_progress)
    elif choice == 3:
        bye_bye()


def end_tournament(tour):
    players = tour.tournament_results()
    tour_v.fin_tournoi_affichage(players)


def bye_bye():
    sys.exit()
