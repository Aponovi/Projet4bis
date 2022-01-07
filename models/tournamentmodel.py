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
        self.ronde = []
        self.time = time
        self.description = description
        self.nb_players = nb_players
        self.turn_number = turn_number
        self.players = []
        if id_tournament == "":
            self.id_tournament = uuid.uuid4()
        else:
            self.id_tournament = uuid.UUID(id_tournament)

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
            tournaments.append(TournamentModel.deserialized_tournament(serialized_tournament))
        return tournaments

    @staticmethod
    def load_last_tournament():
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        serialized_tournaments = tournaments_table.all()
        for serialized_tournament in serialized_tournaments:
            if serialized_tournament["tournament_over"] == "False":
                return TournamentModel.deserialized_tournament(serialized_tournament)

    @staticmethod
    def deserialized_tournament(serialized_tournament):
        return TournamentModel(name=serialized_tournament["name"],
                               place=serialized_tournament["place"],
                               start_date=serialized_tournament["start_date"],
                               end_date=serialized_tournament["end_date"],
                               round_instances=serialized_tournament["round_instances"],
                               time=serialized_tournament["time"],
                               description=serialized_tournament["description"],
                               nb_players=serialized_tournament["nb_players"],
                               turn_number=serialized_tournament["turn_number"],
                               id_tournament=serialized_tournament["id_tournament"],
                               tournament_over=serialized_tournament["tournament_over"]
                               )

    def maj_tournament_over(self):
        db = TinyDB("db.json")
        table = db.table("tournaments")
        table.update({"tournament_over": str(self.tournament_over)}, where("id_tournament") == self.id_tournament.hex)

    def add_player(self, player):
        self.players.append(player)

    def tournament_results(self):
        """Cumule les scores des joueurs"""
        players_scores = {}
        for tour in self.round_instances:
            for match in tour:
                first_element = match[0]
                second_element = match[1]
                premier_joueur = first_element[0]
                deuxieme_joueur = second_element[0]
                if premier_joueur in players_scores:
                    players_scores[premier_joueur] += first_element[1]
                else:
                    players_scores[premier_joueur] = first_element[1]
                if deuxieme_joueur in players_scores:
                    players_scores[deuxieme_joueur] += second_element[1]
                else:
                    players_scores[deuxieme_joueur] = second_element[1]
        """Tri les joueurs selon leur score et leur classement"""
        players_scores_trie = []
        while len(players_scores) > 0:
            max_score = 0
            joueur_max_score = None
            for joueur in players_scores:
                if joueur_max_score is None:
                    max_score = players_scores[joueur]
                    joueur_max_score = joueur
                else:
                    if players_scores[joueur] > max_score:
                        max_score = players_scores[joueur]
                        joueur_max_score = joueur
                    elif players_scores[joueur] == max_score:
                        if joueur.ranking > joueur_max_score.ranking:
                            joueur_max_score = joueur
            players_scores_trie.append((joueur_max_score, players_scores[joueur_max_score]))
            del players_scores[joueur_max_score]
        return players_scores_trie

