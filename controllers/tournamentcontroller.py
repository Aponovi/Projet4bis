from controllers import menucontroller
from views import tournamentview as tournament_view, menuview as view_menu
from models.tournamentmodel import TournamentModel as Tournament_model
from models.playermodel import Player as Player_model

class TournamentController:

    def __init__(self):
        self.view = tournament_view.TournamentView()

    def tournament_creation(self):
        name, place, start_date, end_date, time_control, description = self.view.new_tournament()
        new_tournament = Tournament_model(name=name,
                                          place=place,
                                          start_date=start_date,
                                          end_date=end_date,
                                          round_instances=[],
                                          time=time_control,
                                          description=description)

        for i in range(8):
            new_player = tournament_view.tournament_players(new_tournament)
            player = Player_model(name=new_player[1],
                                  first_name=new_player[2],
                                  birth_date=new_player[3],
                                  gender=new_player[4],
                                  ranking=new_player[5])
            new_tournament.add_player(player)
        menucontroller.menu_tournament(new_tournament)

    @staticmethod
    def tournament_creation_test():
        new_tournament = Tournament_model(name="name",
                                          place="place",
                                          start_date="22/10/2021",
                                          end_date="22/10/2021",
                                          round_instances=[],
                                          time="Bullet",
                                          description="description")

        for i in range(8):
            player = Player_model(name="name" + str(i),
                                  first_name="first_name" + str(i),
                                  birth_date="22/10/2021",
                                  gender="f",
                                  ranking=i * 2 + 404)
            new_tournament.add_player(player)
        menucontroller.menu_tournament(new_tournament)
