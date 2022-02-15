import uuid

from tinydb import TinyDB, where


class Player:
    """Modèle représentant un joueur."""

    def __init__(self, name, first_name, birth_date, gender, ranking,
                 id_tournament, id_player=""):
        """Initialise les détails relatifs au joueur."""
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        if id_player == "":
            self.id_player = uuid.uuid4()
        else:
            self.id_player = uuid.UUID(id_player)
        self.id_tournament = id_tournament

    def serialized_player(self):
        return {
            'name': self.name,
            'first_name': self.first_name,
            'birth_date': str(self.birth_date),
            'gender': self.gender,
            'ranking': self.ranking,
            'id_player': self.id_player.hex,
            'id_tournament': self.id_tournament.hex
        }

    def save_player(self):
        serialized_player = self.serialized_player()
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(serialized_player)

    @staticmethod
    def load_players(order_by_ranking=False):
        db = TinyDB("db.json")
        players_table = db.table("players")
        serialized_players = players_table.all()
        players = []
        for serialized_player in serialized_players:
            players.append(Player.deserialized_player(serialized_player))
        if order_by_ranking is False:
            players = sorted(players, key=lambda player: player.name)
        elif order_by_ranking is True:
            players = sorted(players, key=lambda player: player.ranking)
        return players

    @staticmethod
    def load_player(id_player):
        db = TinyDB("db.json")
        players_table = db.table("players")
        serialized_players = players_table.all()
        for serialized_player in serialized_players:
            if serialized_player["id_player"] == id_player.hex:
                return Player.deserialized_player(serialized_player)

    @staticmethod
    def load_players_by_tournament(id_tournament):
        players = Player.load_players()
        players_tournament = []
        for i in range(len(players)):
            if players[i].id_tournament == id_tournament.hex:
                players_tournament.append(players[i])
        return players_tournament

    @staticmethod
    def deserialized_player(serialized_player):
        return Player(name=serialized_player["name"],
                      first_name=serialized_player["first_name"],
                      birth_date=serialized_player["birth_date"],
                      gender=serialized_player["gender"],
                      ranking=serialized_player["ranking"],
                      id_tournament=serialized_player["id_tournament"],
                      id_player=serialized_player["id_player"])

    def update_ranking(self, new_ranking):
        self.ranking = new_ranking
        db = TinyDB("db.json")
        table = db.table("players")
        table.update({"ranking": str(self.ranking)},
                     where("id_player") == self.id_player.hex)
