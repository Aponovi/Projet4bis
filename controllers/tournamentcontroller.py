from controllers import menucontroller
from views import tournamentview as tournament_view
from models.tournamentmodel import TournamentModel as Tournament_model
from models.playermodel import Player as Player_model


class TournamentController:

    def __init__(self):
        self.view = tournament_view.TournamentView()

    def tournament_creation(self):
        (name, place, start_date, end_date, time_control, description,
         nb_players, nb_rounds) = self.view.new_tournament()
        new_tournament = Tournament_model(name=name,
                                          place=place,
                                          start_date=start_date,
                                          end_date=end_date,
                                          round_instances=[],
                                          time=time_control,
                                          description=description,
                                          nb_players=nb_players,
                                          turn_number=nb_rounds, )
        new_tournament.save_tournament()
        for i in range(nb_players):
            new_player = tournament_view.tournament_players(new_tournament)
            player = Player_model(name=new_player[1],
                                  first_name=new_player[2],
                                  birth_date=new_player[3],
                                  gender=new_player[4],
                                  ranking=new_player[5],
                                  id_tournament=new_tournament.id_tournament)
            player.save_player()
            new_tournament.add_player(player)
        menucontroller.menu_tournament(new_tournament)

    @staticmethod
    def tournament_creation_test():
        new_tournament = Tournament_model(name="name1",
                                          place="place1",
                                          start_date="22/10/2021",
                                          end_date="22/10/2021",
                                          round_instances=[],
                                          time="Bullet",
                                          description="description",
                                          nb_players=8,
                                          turn_number=4, )
        new_tournament.save_tournament()

        for i in range(8):
            player = Player_model(name="name" + str(i),
                                  first_name="first_name" + str(i),
                                  birth_date="22/10/2021",
                                  gender="f",
                                  ranking=i * 2 + 404,
                                  id_tournament=new_tournament.id_tournament)
            new_tournament.add_player(player)
            player.save_player()
        menucontroller.menu_tournament(new_tournament)
