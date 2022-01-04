import datetime
import uuid

from tinydb import TinyDB

from models import matchmodel


class Round:
    """Modèle représentant un tour."""

    def __init__(self, nb_round_past, id_tournament, id_round="", name="", start_date="", end_date=""):
        if name == "":
            self.name = "Round " + str(nb_round_past+1)
        else:
            self.name = name
        if start_date == "":
            self.start_date = datetime.datetime.now()
        else:
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f")
        if end_date == "" or end_date == "None":
            self.end_date = None
        else:
            self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S.%f")
        self.matches = None
        self.id_tournament = id_tournament
        if id_round == "":
            self.id_round = uuid.uuid4()
        else:
            self.id_round = uuid.UUID(id_round)

    def serialized_round(self):
        return {
            'name': self.name,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'id_tournament': self.id_tournament.hex,
            'id_round': self.id_round.hex
            }

    @staticmethod
    def deserialized_round(serialized_round):
        return Round(
            nb_round_past=0,
            id_tournament=uuid.UUID(serialized_round["id_tournament"]),
            id_round=serialized_round["id_round"],
            name=serialized_round["name"],
            start_date=serialized_round["start_date"],
            end_date=serialized_round["end_date"])

    def generate_first_pair(self, players, round_row):
        """Premières paires générées selon le système de tournoi suisse"""
        nb_players = len(players)
        # tri des joueurs par classement
        players = sorted(players, key=lambda player: player.ranking, reverse=True)
        middle_list = int(nb_players / 2)
        players_sup = players[0: middle_list]
        players_inf = players[middle_list:nb_players]
        nb_matches = len(players_sup)
        for index in range(nb_matches):
            # competitors = ([players_sup[index], 0], [players_inf[index], 0])
            competitors = matchmodel.Match(players_sup[index], 0, players_inf[index], 0, self.id_round)
            round_row.append(competitors.match_tuple())

    @staticmethod
    def sorting_players(round_instances):
        """Cumule les scores des joueurs"""
        players_scores = {}
        for tour in round_instances:
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
        players = []
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
            players.append(joueur_max_score)
            del players_scores[joueur_max_score]
        return players

    def pair_player(self, players, round_instance, round_row):
        nb_players = len(players)
        players = self.sorting_players(round_instance)
        nb_matches = int(nb_players / 2)
        index_player_1 = 0
        index_player_2 = 1
        index_player_2_tmp = 1
        previous_matches = []
        for m in range(nb_matches):
            # recherche dans round_instance les matches précédents pour savoir si les joueurs se sont déjà rencontrés
            while matchmodel.Match.historic_match(round_instance, index_player_1, index_player_2_tmp, players):
                index_player_2_tmp += 1
                if index_player_2_tmp > nb_players - 1:
                    index_player_2_tmp = index_player_2
                    break
            index_player_2 = index_player_2_tmp
            competitors = matchmodel.Match(players[index_player_1], 0, players[index_player_2], 0, self.id_round)
            round_row.append(competitors.match_tuple())
            previous_matches.append(index_player_1)
            previous_matches.append(index_player_2)

            # joueur in self.players avec plus petit indice n'ayant pas encore de match
            for ind in range(len(players)):
                if ind not in previous_matches:
                    index_player_1 = ind
                    break
            for ind in range(index_player_1 + 1, len(players)):
                if ind not in previous_matches:
                    index_player_2 = ind
                    index_player_2_tmp = ind
                    break

    def generate_pair(self, players, round_instance):
        nb_players = len(players)
        if nb_players % 2 == 0 and nb_players > 0:
            round_row = []
            if len(round_instance) == 0:
                self.generate_first_pair(players, round_row)
            else:
                self.pair_player(players, round_instance, round_row)
            self.matches = round_row

            round_instance.append(round_row)

    @staticmethod
    def load_round():
        db = TinyDB('db.json')
        rounds_table = db.table('rounds')
        serialized_rounds = rounds_table.all()
        rounds = []
        for serialized_round in serialized_rounds:
            rounds.append(Round.deserialized_round(serialized_round))
        return rounds
