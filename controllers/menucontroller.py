from models import tournamentmodel, playermodel
from views import menuview, tournamentview
from controllers import tournamentcontroller, roundcontroller, playercontroller, reportscontroller


def start_program():
    tournament = tournamentmodel.TournamentModel.load_last_tournament()
    tournament.players = playermodel.Player.load_players_by_tournament(tournament.id_tournament)
    menuview.welcome()
    choice = menuview.main_menu()

    if choice == 1:
        controller_tournament = tournamentcontroller.TournamentController()
        controller_tournament.tournament_creation()

    elif choice == 3:
        controller_tournament = tournamentcontroller.TournamentController()
        controller_tournament.tournament_creation_test()

    elif choice == 2:
        controller_reports = reportscontroller.ReportsController()
        choice_reports = menuview.reports_menu()
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


def menu_tournament(tournament, round_in_progress=False):
    choice = menuview.tournament_menu(round_in_progress)
    if choice == 1:
        if not round_in_progress:
            """Générer une ronde"""
            round_controller = roundcontroller.RoundController()
            round_controller.round_creation(tournament)
        else:
            """Saisir les scores de la ronde"""
            round_controller = roundcontroller.RoundController()
            round_controller.round_results(tournament)
    elif choice == 2:
        """Mettre à jour classement"""
        player_controller = playercontroller.PlayerController()
        player_controller.update_ranking(tournament, round_in_progress)


def fin_tournament(tournament):
    players = tournament.tournament_results()
    tournamentview.fin_tournoi_affichage(players)
