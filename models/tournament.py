import uuid

from tinydb import TinyDB, where


class TournamentModel:
    """Modèle représentant un tournoi."""

    def __init__(self, name, place, start_date, end_date,
                 round_instances, time, description, nb_players, turn_number=4,
                 id_tournament="", tournament_over=False):
        """Initialise les détails relatifs au tournoi."""
        self.tournament_over = tournament_over
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_instances = round_instances
        self.turn = []
        self.time = time
        self.description = description
        self.nb_players = nb_players
        self.turn_number = turn_number
        self.players = []
        if id_tournament == "":
            self.id_tournament = uuid.uuid4()
        else:
            self.id_tournament = uuid.UUID(id_tournament)

    def save_tournament(self):
        serialized_tournaments = []
        serialized_tournament = self.serialized_tournament()
        serialized_tournaments.append(serialized_tournament)
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        tournaments_table.insert_multiple(serialized_tournaments)

    def serialized_tournament(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'round_instances': self.round_instances,
            'time': self.time,
            'description': self.description,
            'nb_players': self.nb_players,
            'turn_number': self.turn_number,
            'id_tournament': self.id_tournament.hex,
            'tournament_over': self.tournament_over
        }

    @staticmethod
    def load_tournaments():
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        serialized_tournaments = tournaments_table.all()
        tournaments = []
        for serialized_tournament in serialized_tournaments:
            tournaments.append(TournamentModel
                               .deserialized_tournament(serialized_tournament))
        return tournaments

    @staticmethod
    def load_last_tournament():
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        serialized_tournaments = tournaments_table.all()
        for serialized_tournament in serialized_tournaments:
            if not serialized_tournament["tournament_over"]:
                return TournamentModel\
                    .deserialized_tournament(serialized_tournament)

    @staticmethod
    def deserialized_tournament(srz_tour):
        return TournamentModel(name=srz_tour["name"],
                               place=srz_tour["place"],
                               start_date=srz_tour["start_date"],
                               end_date=srz_tour["end_date"],
                               round_instances=srz_tour["round_instances"],
                               time=srz_tour["time"],
                               description=srz_tour["description"],
                               nb_players=srz_tour["nb_players"],
                               turn_number=srz_tour["turn_number"],
                               id_tournament=srz_tour["id_tournament"],
                               tournament_over=srz_tour["tournament_over"]
                               )

    def maj_tournament_over(self):
        db = TinyDB("db.json")
        table = db.table("tournaments")
        table.update({"tournament_over": str(self.tournament_over)},
                     where("id_tournament") == self.id_tournament.hex)

    def add_player(self, player):
        self.players.append(player)

    def tournament_results(self):
        """Cumule les scores des joueurs"""
        players_scores = {}
        for tour in self.round_instances:
            for match in tour:
                first_element = match[0]
                second_element = match[1]
                first_player = first_element[0]
                second_player = second_element[0]
                if first_player in players_scores:
                    players_scores[first_player] += float(first_element[1])
                else:
                    players_scores[first_player] = float(first_element[1])
                if second_player in players_scores:
                    players_scores[second_player] += float(second_element[1])
                else:
                    players_scores[second_player] = float(second_element[1])
        """Tri les joueurs selon leur score et leur classement"""
        players_scores_trie = []
        while len(players_scores) > 0:
            max_score = 0
            player_max_score = None
            for player in players_scores:
                if player_max_score is None:
                    max_score = players_scores[player]
                    player_max_score = player
                else:
                    if players_scores[player] > max_score:
                        max_score = players_scores[player]
                        player_max_score = player
                    elif players_scores[player] == max_score:
                        if player.ranking > player_max_score.ranking:
                            player_max_score = player
            players_scores_trie\
                .append((player_max_score, players_scores[player_max_score]))
            del players_scores[player_max_score]
        return players_scores_trie
