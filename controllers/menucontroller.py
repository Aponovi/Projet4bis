from views import menuview
from controllers import tournamentcontroller, roundcontroller


def start_program():
    menuview.welcome()
    choice = menuview.main_menu()

    if choice == 1:
        controller_tournament = tournamentcontroller.TournamentController()
        controller_tournament.tournament_creation()

    elif choice == 4:
        controller_tournament = tournamentcontroller.TournamentController()
        controller_tournament.tournament_creation_test()
    # elif choice == 2:
    #     controllers.update_ranking()
    # elif choice == 3:
    # controllers.display_reports()


def menu_tournament(tournament, round_in_progress=False):
    choice = menuview.tournament_menu(round_in_progress)
    if choice == 1:
        if not round_in_progress:
            """générer une ronde"""
            round_controller = roundcontroller.RoundController()
            round_controller.round_creation(tournament)
        else:
            """saisir les scores de la ronde"""
            round_controller = roundcontroller.RoundController()
            round_controller.round_results(tournament)
    elif choice == 2:
        """Mettre à jour classement"""
